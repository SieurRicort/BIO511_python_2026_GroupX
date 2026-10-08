#!usr/bin/python3

######## FOR LOOPS BOOP

## Input /BIO511_python_2026_GroupX/prac1/carolina/datatypes_caro.py
import fileinput

# define input file and empty list variable
input_file = '/home/DNebula/python_practicals/BIO511_python_2026_GroupX/prac1/carolina/datatypes_caro.py'
datatypeslist = list()

# init for loop
for line in fileinput.input(files=input_file):
    print(line, end='datatypeslist') # Where did this line come from? Why?
    datatypeslist.append(line) # exchange line for ?


print(datatypeslist)
type(datatypeslist)
