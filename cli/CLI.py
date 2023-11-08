import importlib
from commands.basic import ImportCommand
from .ValidateInput import InputAdapter
from user.User import User
import json

class CLI:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(CLI, self).__new__(self)
        return self.instance

    def __init__(self):
        self.import_command = ImportCommand()
        self.input_adapter = InputAdapter(self.import_command.available_commands.items())
        self.user = None

    def auth(self):
        username = input('Enter username: ')
        password = input('Enter password: ')

        with open("data/users.json", "r") as json_file:
            loaded_users = json.load(json_file)

        for user_data in loaded_users:
            if user_data['username'] == username and user_data['password'] == password:
                is_admin = user_data['is_admin']
                message = user_data['message']
                user = User(username, password, is_admin, message)
                CLI.instance.user = user
                print(f'Welcome, {self.user.username}')
                return

        print('Invalid credentials! Try again')
        return self.auth()
    
    def logout(self):
        self.user = None


    def run(self):
        self.import_command.import_commands()
        
        while True:
            
            if self.user is None:
                self.auth()
            
            print("\nAvailable commands:")

            for name, description in self.import_command.available_commands.items():
                is_admin_command = self.import_command.available_commands[name]['admin'] == True
                if self.user and self.user.is_admin and is_admin_command:
                    print(f"{description['id']}) {name}: {description['description']}")
                elif not self.user or (not self.user.is_admin and not is_admin_command):
                    print(f"{description['id']}) {name}: {description['description']}")
                
                

            choice = input("Enter a command name or ID or 'exit' to quit or 'logout' to logout: ")
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
            
            if choice == 'logout':
                print('You have logged out')
                self.user = None
            