import importlib
import inspect

class Command:
    def __init__(self, name, description, admin):
        self.name = name
        self.description = description
        self.admin = admin

    def execute(self, args):
        pass


class ImportCommand:
    def __init__(self):
        self.available_commands = {}

    def import_commands(self):
        import os
        import sys

        commands_folder = "commands"
        i = 1
        if os.path.exists(commands_folder) and os.path.isdir(commands_folder):
            sys.path.append(commands_folder)
            for filename in os.listdir(commands_folder):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = filename[:-3]
                    module = importlib.import_module(f"{commands_folder}.{module_name}")

                    for name, obj in inspect.getmembers(module):
                        if inspect.isclass(obj) and issubclass(obj, Command) and obj is not Command:
                            command_name = getattr(obj, "command_name", name)
                            command_description = getattr(obj, "command_description", name)
                            admin = getattr(obj, 'admin', name)
                            self.available_commands[command_name] = {
                                'id' : i,
                                'class': obj,
                                'description': command_description,
                                'admin' : admin
                            }
                            i+=1


    def list_available_commands(self):
        print("Available commands:")
        for name, description in self.available_commands.items():
            print(f"{name}: {description}")

