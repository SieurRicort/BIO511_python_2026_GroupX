#!/usr/bin/env python3

#----------------
# How to
# python3 append_row.py <file.csv> <content>
#-----------------

# Import modules
import sys
import csv

file=sys.argv[1]
delim=sys.argv[2]

def append_csv():

    append=sys.argv[3:]
    

    with open(file, mode='a', newline='') as edit_file:
        writer = csv.writer(edit_file, delimiter=delim) # creates as many rows as we input using , as a delimiter
        writer.writerow(append)

    print(f"Row succesfully appended to '{file}'.")

append_csv()