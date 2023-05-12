class Book:
    def __init__(self, title : str, author : str, num_pages : str, type : str) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.type = type
        
    def print_info(self):
        print("=========The information of the book are as follow=========")
        print("Title - ", self.title)
        print("Authour - ", self.author)
        print("Number of pages - ", self.num_pages)
        print("Type - ", self.type)

        
class Library:
    def __init__(self) -> None:
        self.books_list = []
    def add_book(self, book : Book) -> None:
        self.books_list.append(book)
    def print_books(self) -> None:
        for b in self.books_list:
        b.print_info()
    def borrow_book(self, title : str) -> Book:
        for b in self.books_list:
        if b.title.lower() == title.lower():
            self.books_list.remove(b)
            return b
        return None

library = Library()
book_f = open("library.txt", 'r')
lines = book_f.readlines()
book_f.close()

for line in lines:
    curr_book = line.split(sep = ',') # field of books are separated by a comma
    book = Book(curr_book[0], curr_book[1], curr_book[2], curr_book[3])
    library.add_book(book)
    library.print_books()
    
while True:
    book_to_borrow = input('Title of Book to borrow ')
    borrowed_book = library.borrow_book(book_to_borrow)
    if borrowed_book != None:
        break
    borrowed_book.print_info()