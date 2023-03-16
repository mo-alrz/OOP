# Write a program which can store books in a library.
# Every library has a name and can store multiple books.
# Every book has a title, an author, a release year and a weight.
# The library must provide the following functionalities:
# We can add books to the library
# We want to be able to remove a book by title
# We also want to be able to get the books that were released in a given year
# We also want to be able to get the lightest book
# Using your solution, the following code should run without errors and print the expected results.


class Book:
    def __init__(self, title, author, rel_date, weight):
        self.title = title
        self.author = author
        self.rel_date = rel_date
        self.weight = weight

    def __str__(self):
        return f'{self.title} {self.author} {self.rel_date} {self.weight}'


class Library:
    books = []

    def __init__(self, name):
        self.name = name

    def add(self, book: Book):
        self.books.append(book)

    def get_books_by_year(self, year):
        counter = []
        for i in self.books:
            if i.rel_date == year:
                counter.append(i)
        return counter

    def get_lightest(self):
        lightest_book = min(self.books, key=lambda b: b.weight)
        return lightest_book

    def remove(self, book_title):
        for i in self.books:
            if i.title == book_title:
                self.books.remove(i)


library = Library("City Central")
library.add(Book("Life of A", "A", 2000, 8))
library.add(Book("Life of B", "B", 2000, 10))
library.add(Book("Life of C", "C", 2001, 12))
library.add(Book("Life of D", "D", 2002, 16))
print(len(library.get_books_by_year(2000)))  # should print: 2
print(library.get_lightest())  # should print: Life of A
library.remove("Life of A")
library.add(Book("Life of D", "D", 2002, 2))
print(len(library.get_books_by_year(2000)))  # should print: 1
print(library.get_lightest())  # should print: Life of D
