class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)

        self.file_size =file_size

        def __str__(self):
             return f"Ebook: '{self.title}' by {self.author} - {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(self, title, author)
        self.page_count =page_count

        def __str__(self):
            return f"book: '{self.title}'  by'{self.author}' has {self.page_caount} pages"

class Library:
    def __init__(self):
        self.book =[]

    def add_book (self, book):
        for book in self.book:
            if book.title.lower() == book.title.lower and book.author.lower() == book.author.lower():
                print(f"{book.tile} by {book.author} already exists in the library")
                return
            self.book.append(book)
            print(f"{self.title} by {self.author} has been added to the library")

    def list_books (self, book):
        if not self.book:
            print(f"{book.title} by {book.author} in not on the list")
            return
        else:
            print("\n Books in library list")

            for index, book in enumerate(self.book, start=1):
                print(f"{index} . book")        
  
