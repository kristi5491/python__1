class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
    
    def getBook(self):
        book = Book()

        format = self.__builder.get_format()
        book.set_format(format)

        while True :
            page = self.__builder.get_page()
            if page == 'quit':
                break
            book.set_page(page)
        return book



class Builder:
    def get_format(self): pass
    def get_page(self): pass
    
class Book:
    def __init__(self):
        self.__format = None
        self.__pages = list()

    def set_format(self, format):
        self.__format = format
    
    def set_page (self, page):
        self.__pages.append(page)

class CreateBook(Builder):
    def get_format(self):
        format = input('input format: ')
        return format
    def get_page(self):
        page = input('input page: ')
        return page





director = Director()

class LinkedBook:
    def __init__(self, book_desc, pages):
        self.book_description = book_desc
        self.book_pages = pages


class AbstractLibrary:
    def sell(self):
        raise Exception("no books to sell")
class ScienceBook(AbstractLibrary):
    def usedLitList(self, used_list):
        self.used_list = used_list
    def add_glossarium(self, glossarium ):
        self.glossarium = glossarium
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return (f"{self.name}")
class NovelBook(AbstractLibrary):
    def character_list(self, list):
        self.char_list = list
    def brief_description(self, desc):
        self.brief_desc = desc
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return (f"{self.name}")
class ManualBook(AbstractLibrary):
    def add_image(self, image):
        self.image = image
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return (f"{self.name}")
    
class AbstractLibraryFactory:
    def create(self):
        raise Exception("this is not book class")
class ScienceBookFactory(AbstractLibraryFactory):
    def create(self):
        book_desc = ScienceBook('Science Book')
        book_desc.usedLitList(input('input list of literature:'))
        book_desc.add_glossarium(input('input glossarium:'))
        director.setBuilder(CreateBook())
        book_pages = director.getBook()
        full_book = LinkedBook(book_desc, book_pages)
        return full_book
class NovelBookFactory(AbstractLibraryFactory):
    def create(self):
        book = NovelBook('Novel Book')
        book.character_list(input('input character list:'))
        book.brief_description(input('input brief description:'))
        director.setBuilder(CreateBook())
        book_pages = director.getBook()
        full_book = LinkedBook(book, book_pages)
        return full_book     
class ManualBookFactory(AbstractLibraryFactory):
    def create(self ):
        book = ManualBook('Manual Book')
        book.add_image(input('input image:'))
        director.setBuilder(CreateBook())
        book_pages = director.getBook()
        full_book = LinkedBook(book, book_pages)
        return full_book
    
def create_book(bookFactory: AbstractLibraryFactory):
    return bookFactory.create()

scienceBook = create_book(ScienceBookFactory())











