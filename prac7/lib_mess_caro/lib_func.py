import csv



# Creates class of book for library, 
class Book:
    book = []
    def load_from_csv(self, filename):
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
    def __init__(self, title, author, year, copies, lent=0):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.lent = lent
        return self.book
#        self.available = available
    @property
    def available(self):
        return self.copies - self.lent
    
    def __str__(self):
            if self.available > 0:
               return f"{self.title} by {self.author} is in the library"
            else:
               return f"We are sorry, we cannot find any copies of {self.title} by {self.author}" 
    print(book)
    pass


class Library(Book):
    def __init__(self, Book):
        self.books = []



"""
class Member:
    def __init__(self, given, last):
        self.given = given
        self.last = last
        self.borrowed.books
        pass

class Librarian:
"""