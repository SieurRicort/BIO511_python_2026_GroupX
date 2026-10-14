#!usr/bin/python3
# Class creation exercise

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
print(Book)

My_book = Book("Name", "Person", "1000")
print(My_book.year)
