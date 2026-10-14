#!usr/bin/python3
# Class creation exercise
import csv
import os










# Creates class of book for library, 
class Book:
    def __init__(self, title, author, year, available): #, copies, lent):

        self.title = title
        self.author = author
        self.year = year
        self.available = available
#        self.copies = copies
#        self.lent = lent

    
    
        #self.age = age_now(Book)
        print(Book(title))
        pass
    


class Library:
    def __init__(self, filename):
        self.books = []
    def load_from_csv(self, filename):
        filename = file.fileinput()
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                book = Book(
                    title=row["title"],
                    author=row["author"],
                    year=row["row"],
                    available=row["available"].lower(),
                                )
        pass








class Member:
    def __init__(self, given, last):
        self.given = given
        self.last = last
        self.borrowed.books

"""
def age_now(self):
    self.date - self.year
    return age



def add_attr(self):
    sum = number1 + number2
    return sum


My_book = Book("Name", "Person", "1000")
print(My_book.year)


#_______________________________________________________
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        print(number1, number2)
    def add(self):
        sum = self.number1 + self.number2
     #   print(sum)
    def subtract(self):
        sub = self.number1 - self.number2
     #   print(sub)
    def multiply(self):
        product = self.number1 * self.number2
     #   print(product)
    pass
    


my_calc = Calculator(4,6)
print(p"{self.number1} + {self.number2} = {my_calc.add()}")
my_calc.subtract()
my_calc.multiply()


#_____________________________________________

class Circle:
    def __init__(self, radius):
"""