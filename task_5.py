class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.pages_read = 0

    def read(self, pages_read: int) -> float:
        self.pages_read += pages_read
        percent_read = (self.pages_read / self.pages) * 100
        return percent_read


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)


book1 = Book(title="Записки из подполья", author="Ф. М. Достоевский", pages=250)
book2 = Book(title="Computer Networks", author="Andrew S. Tanenbaum", pages=960)

library = Library()
library.add_book(book1)
library.add_book(book2)

percent_read_book1 = book1.read(150)
print(f"{book1.title} by {book1.author}: {percent_read_book1:.2f}% read")

percent_read_book2 = book2.read(200)
print(f"{book2.title} by {book2.author}: {percent_read_book2:.2f}% read")
