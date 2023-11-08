import importlib
from commands.basic import ImportCommand
from commands import MyCustomCommand
from .ValidateInput import InputAdapter

class CLI:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(CLI, self).__new__(self)
        return self.instance

    def __init__(self):
        self.import_command = ImportCommand()
        self.input_adapter = InputAdapter(self.import_command.available_commands.items())

    def run(self):
        self.import_command.import_commands()
        
        while True:
            print("\nAvailable commands:")
            for name, description in self.import_command.available_commands.items():
                print(f"{description['id']}) {name}: {description['description']}")

            choice = input("Enter a command name or ID or 'exit' to quit: ")
            converted_input = self.input_adapter.adapt_input(choice)

            

            if choice == 'exit':
                print("Exiting CLI.")
                break

            if converted_input in self.import_command.available_commands:
                command_class = self.import_command.available_commands[converted_input]['class']
                command_instance = command_class()
                command_instance.execute([])
            else:
                print("Invalid command. Please try again.")