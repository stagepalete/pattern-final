from .basic import Command
from main import library

class AddLibraryItem(Command):
    command_name = "AddItemToLibrary"
    command_description = "Add Book, Magazine or Dvd to library"
    def __init__(self):
        super().__init__(self.command_name, self.command_description)

    def execute(self, args):
        library.add_item()


class DisplayLibraryItems(Command):
    command_name = "DisplayAllItems"
    command_description = "Display all library items"
    def __init__(self):
        super().__init__(self.command_name, self.command_description)

    def execute(self, args):
        library.display_items()

class DisplayBooks(Command):
    command_name = "DisplayAllBooks"
    command_description = "Display all library books"
    def __init__(self):
        super().__init__(self.command_name, self.command_description)

    def execute(self, args):
        library.display_books()

class DisplayDvds(Command):
    command_name = "DisplayAllDvds"
    command_description = "Display all library Dvds"
    def __init__(self):
        super().__init__(self.command_name, self.command_description)

    def execute(self, args):
        library.display_dvds()

class DisplayMagazines(Command):
    command_name = "DisplayAllMagazines"
    command_description = "Display all library Magazines"
    def __init__(self):
        super().__init__(self.command_name, self.command_description)

    def execute(self, args):
        library.display_magazines()

class RemoveItem(Command):
    command_name = "RemoveItemByTitle"
    command_description = "Removes item in library by title"
    def __init__(self):
        super().__init__(self.command_name, self.command_description)

    def execute(self, args):
        library.remove_item(input('Enter the title: '))