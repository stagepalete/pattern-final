from .basic import Command
from main import library
from user.User import User
from cli.CLI import CLI
import json


class Notify(Command):
    command_name = "Notify"
    command_description = "Notify Users"
    admin = True
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        message = input('Notification message: ')
        library.notify_subscribers(message)




class Subscibe(Command):
    command_name = "Subscribe"
    command_description = "Subscribe to get notifications"
    admin = False
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.add_subscribers(CLI.instance.user)
        print(f'{CLI.instance.user.username} - subscribed to library news')
        
class CancelSubscription(Command):
    command_name = "CancelSubscribe"
    command_description = "Cancel Subscribtion to get notifications"
    admin = False
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.remove_subscribers(CLI.instance.user)
        print(f'{CLI.instance.user.username} - Canceled subscribtion to library news')

class CheckInbox(Command):
    command_name = "CheckInbox"
    command_description = "Check Inbox for notifications"
    admin = False
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        CLI.instance.user.update()

class AddLibraryItem(Command):
    command_name = "AddItemToLibrary"
    command_description = "Add Book, Magazine or Dvd to library"
    admin = True
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.add_item()


class DisplayLibraryItems(Command):
    command_name = "DisplayAllItems"
    command_description = "Display all library items"
    admin = False
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.display_items()

class DisplayBooks(Command):
    command_name = "DisplayAllBooks"
    command_description = "Display all library books"
    admin = False
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.display_books()

class DisplayDvds(Command):
    command_name = "DisplayAllDvds"
    command_description = "Display all library Dvds"
    admin = False
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.display_dvds()

class DisplayMagazines(Command):
    command_name = "DisplayAllMagazines"
    command_description = "Display all library Magazines"
    admin = False
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.display_magazines()

class RemoveItem(Command):
    command_name = "RemoveItemByTitle"
    command_description = "Removes item in library by title"
    admin = True
    def __init__(self):
        super().__init__(self.command_name, self.command_description, self.admin)

    def execute(self, args):
        library.remove_item(input('Enter the title: '))

