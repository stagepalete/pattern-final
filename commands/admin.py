from .basic import Command
from main import library

class AddLibraryItem(Command):
    command_name = "AddItemToLibrary"
    command_description = "Add Book, Magazine or Dvd to library"
    admin = True
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.add_item()


class RemoveItem(Command):
    command_name = "RemoveItemByTitle"
    command_description = "Removes item in library by title"
    admin = True
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.remove_item(input('Enter the title: '))

class Notify(Command):
    command_name = "Notify"
    command_description = "Notify Users"
    admin = True
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        message = input('Notification message: ')
        library.notify_subscribers(message)

class CheckSubscribers(Command):
    command_name = "Notify"
    command_description = "Notify Users"
    admin = True
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        message = input('Notification message: ')
        library.notify_subscribers(message)