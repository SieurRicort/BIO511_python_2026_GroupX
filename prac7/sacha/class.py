#!/usr/bin/env python3

# Import modules
import math

# Book

class Book():
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year
        pass

book1 = Book("TLOTR", "J.R.R Tolkien", 1954)
print(book1.title)

# Parrot

class Parrot():
    def speak(self, text):
        print(f"The parrot says: {text}")
        pass

my_parrot = Parrot()
my_parrot.speak("Gougougaga")

# Calculator

class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.sum=self.add()
        self.product=self.multiply()
        self.quotient=self.divide()

    def add(self):
        sum = (self.num1 + self.num2)
        return sum

    def multiply(self):
        product = (self.num1 * self.num2)
        return product

    def divide(self):
        quotient = (self.num1 / self.num2)
        return quotient

my_calc=Calculator(5,5)
print(my_calc.add())
print(my_calc.product)
print(my_calc.quotient)

# Circle

class Circle():
    count = 0 
    
    def __init__(self):
        self.radius = float(input('Enter the radius of the circle (float in cm): '))
        self.circumference = self.calc_perimeter()
        self.area = self.calc_area()
        self.input1 = input('What do you want to output (perimeter, area, both)? : ')
        self.ask_for_output()
        Circle.count += 1
        self.id = Circle.count

    def calc_perimeter(self):
        circumference = 2 * math.pi * self.radius
        circumference = round(circumference, 2)
        return circumference

    def calc_area(self):
        area = math.pi * (self.radius ** 2)
        area = round(area, 2)
        return area

    def ask_for_output(self):
        if self.input1 == 'perimeter':
            print(f"The perimeter of the circle is {self.circumference} cm")
        elif self.input1 == 'area':
            print(f"The area of the circle is {self.area} cm²")
        elif self.input1 == 'both':
            print(f"The perimeter of the circle is {self.circumference} cm and the area of the circle is {self.area} cm²")
        else: print("Wrong input")


circle=[] # Empty list

for n in range(5): # Create a loop
    circle.append(Circle()) # Store the object of Circle() in the list circle
    print(circle[n].id) # Print the current object id

print(Circle.count) # How many calls of Circle() so far
# Classeption

"""
This will be a 
"""