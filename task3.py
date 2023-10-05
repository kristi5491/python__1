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
    def getFormat(self):
        return self.__format
    def getPages(self):
        return self.__pages
    

class CreateBook(Builder):
    def get_format(self):
        format = input('input format: ')
        return format
    def get_page(self):
        page = input('input page: ')
        return page

class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def add_book_id(self, book):
        count = len(self.book_ids)
        self.book_ids[f'{book.book_description.name}{count + 1}'] = book
    def get_dict(self):
        return self.book_ids 
 
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
            self.book_ids = dict()



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
        book_desc = ScienceBook('Science_Book')
        book_desc.usedLitList(input('input list of literature:'))
        book_desc.add_glossarium(input('input glossarium:'))
        director.setBuilder(CreateBook())
        book_pages = director.getBook()
        full_book = LinkedBook(book_desc, book_pages)
        singl.add_book_id(full_book)
        return full_book
class NovelBookFactory(AbstractLibraryFactory):
    def create(self):
        book = NovelBook('Novel_Book')
        book.character_list(input('input character list:'))
        book.brief_description(input('input brief description:'))
        director.setBuilder(CreateBook())
        book_pages = director.getBook()
        full_book = LinkedBook(book, book_pages)
        singl.add_book_id(full_book)
        return full_book     
class ManualBookFactory(AbstractLibraryFactory):
    def create(self ):
        book = ManualBook('Manual_Book')
        book.add_image(input('input image:'))
        director.setBuilder(CreateBook())
        book_pages = director.getBook()
        full_book = LinkedBook(book, book_pages)
        singl.add_book_id(full_book)
        return full_book
    
def create_book(bookFactory: AbstractLibraryFactory):
    return bookFactory.create()

singl = Singleton()

while True:
    print('\nChoose what you want to do:\n1. Write a book\n2. View librariesу\n3. End the program \n4.generate book')
    choice = input('Введіть відповідь: ')
    match choice:
        case '1':
            print('\nChoose the type of book you will write:\n1. ScienceBook\n2. NovelBook\n3. ManualBook')
            choice = input('Введіть відповідь: ')
            book = None
            match choice:
                case '1':
                    book = create_book(ScienceBookFactory())
                    print('\nYou wrote a Scientific book!')
                case '2':
                    book = create_book(NovelBookFactory())
                    print('\nYou wrote a Novel book!')
                case '3':
                    book = create_book(ManualBookFactory())
                    print('\nYou wrote a Manual book!')
        case '2':
            dictionary = singl.get_dict()
            print('\n')
            for dict in dictionary:
                print(dict)
            print('\n')
            bookName = input('Введіть назву книги з якою хочете взаємодіяти: ')
            if(dictionary.get(bookName) is not None):
                while True:
                    print('\nВиберіть що ви хочете зробити:\n1. Перечитати усю книгу\n2. Повернутись до головного меню\n')
                    choice = input('Введіть відповідь: ')
                    match choice:
                        case '1':
                            pages = dictionary[bookName].book_pages.getPages()
                            i = 1
                            for page in pages:
                                print(f'{i}: {page}')
                                i += 1
                        case '2':
                            break
            else:
                print('\nТакої книги не знайдено!\n') 
        case '3':
            break
        case '4':
            import random
            
            # book = [ScienceBookFactory,NovelBookFactory,ManualBookFactory]
            # random_class = random.choice(book)()
            # random_class.create()

            # import string

            # generate_random_book()
    


            # random_desc = ["красивий", "цікавий", "незабутній", "фантастичний", "неймовірний",
            #    "дивовижний", "улюблений", "вражаючий", "чарівний", "заворожуючий"]
       