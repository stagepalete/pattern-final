from .Items.Items import Book, Magazine, Dvd


class LibraryItemFactory:
    def create_library_item(self, item_type):
        if item_type == "book":
            book = Book()
            book.create_item()
            return book 
        elif item_type == "magazine":
            magazine = Magazine()
            magazine.create_item()
            return magazine
        elif item_type == "dvd":
            dvd = Dvd()
            dvd.create_item()
            return dvd
        else:
            return None
