from .Items.Items import Book, Dvd, Magazine
from .LibraryItemFactory import LibraryItemFactory
from .Subscription import Subscription

class Library(Subscription):
    def __init__(self):
        self.library_items = []
        self.library_item_factory = LibraryItemFactory()
        self.subscribers = []

    def add_item(self):
        item_type = input("Select Item type that you want to choose (book, magazine, dvd): ")
        item = self.library_item_factory.create_library_item(item_type)
        self.library_items.append(item)

    def remove_item(self, title):

        for item in self.library_items:
            if title == item.title:
                self.library_items.remove(item)
                return 
        print(f"{item} is not in the library.")

    def display_items(self):
        for item in self.library_items:
            item.display_info()
    
    def display_books(self):
        for item in self.library_items:
            if isinstance(item, Book):
                item.display_info()

    def display_dvds(self):
        for item in self.library_items:
            if isinstance(item, Dvd):
                item.display_info()

    def display_magazines(self):
        for item in self.library_items:
            if isinstance(item, Magazine):
                item.display_info()
