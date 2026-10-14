#import sys brings in Python’s built-in sys module, 
# which gives access to sys.argv. This is the same idea as the import lines you saw in Practical 4.
#sys.argv[1:] means “the list from item 1 onwards”, so it skips the script name and keeps only your values.
#",".join(values) glues the values together with 
# commas between them: ['1','2','3','4','5'] becomes "1,2,3,4,5".
#+ "\n" ends the line, so the next row starts on a new line.
# open("data.csv", "a") opens the file in append mode, so the 5 existing rows stay.


import sys

values = sys.argv[1:]

with open("data.csv", "a") as f:
    f.write(",".join(values) + "\n")