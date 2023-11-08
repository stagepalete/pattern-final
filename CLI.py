import importlib
from commands.basic import ImportCommand
from commands import MyCustomCommand


class CLI:
    __commands = []

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(CLI, self).__new__(self)
        return self.instance

    def __init__(self):
        self.import_command = ImportCommand()

    def run(self):
        self.import_command.import_commands()
        
        while True:
            print("\nAvailable commands:")
            for name, description in self.import_command.available_commands.items():
                print(f"{name}: {description['description']}")

            choice = input("Enter a command or 'exit' to quit: ")

            if choice == 'exit':
                print("Exiting CLI.")
                break

            if choice in self.import_command.available_commands:
                command_class = self.import_command.available_commands[choice]['class']
                command_instance = command_class()
                command_instance.execute([])
            else:
                print("Invalid command. Please try again.")