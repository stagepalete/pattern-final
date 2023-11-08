from .basic import Command

class MyCustomCommand(Command):
    command_name = "mycommand"
    command_description = "Description of MyCustomCommand"
    def __init__(self):
        super().__init__(self.command_name, self.command_description)

    def execute(self, args):
        # Implement the specific behavior of your command here
        print("MyCustomCommand executed.")
