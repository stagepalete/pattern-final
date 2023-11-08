from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def create_item(self):
        pass

    @abstractmethod
    def delete_item(self):
        pass
    
    @abstractmethod
    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self):
        self.title = None
        self.author = None
        self.isbn = None
    
    def create_item(self):
        self.title = input("Enter the title: ")
        self.author = input("Enter the author: ")
        self.isbn = input("Enter the ISBN: ")
        print("Book item created.")
    
    def delete_item(self):
        if self.title:
            self.title = None
            self.author = None
            self.isbn = None
            print("Book item deleted.")
        else:
            print("No book item to delete.")

    def display_info(self):
        if self.title:
            print(f"Book: Title - {self.title}, Author - {self.author}, ISBN - {self.isbn}")
        else:
            print("Book: No item created.")

class Magazine(LibraryItem):
    def __init__(self):
        self.title = None
        self.Date = None
        self.Publisher = None
    
    def create_item(self):
        self.title = input("Enter the title: ")
        self.Date = input("Enter the Date: ")
        self.Publisher = input("Enter the Publisher: ")
        print("Book item created.")

    def delete_item(self):
        if self.title:
            self.title = None
            self.Date = None
            self.Publisher = None
            print("Magazine item deleted.")
        else:
            print("No Magazine item to delete.")
    
    def display_info(self):
        print(f"Magazine: Title - {self.title}, Issue Date - {self.Date}, Publisher - {self.Publisher}")


class Dvd(LibraryItem):

    def __init__(self):
        self.title = None
        self.Date = None
        self.Director = None

    def create_item(self):
        self.title = input("Enter the title: ")
        self.Date = input("Enter the Date: ")
        self.Director = input("Enter the Director: ")
        print("Book item created.")

    def delete_item(self):
        if self.title:
            self.title = None
            self.Date = None
            self.Director = None
            print("DVD item deleted.")
        else:
            print("No DVD item to delete.")

    def display_info(self):
        print(f"DVD: Title - {self.title}, Date - {self.Date}, Director - {self.Director}")