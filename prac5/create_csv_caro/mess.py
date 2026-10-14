#!/usr/bin/env python3
# Calls on create_array.py and converts array to .csv
#if __name__ == __main__:
#    main()

#from modules.create_empty  import empty_array
import argparse
import os 
#import csv
#import pathlib
import numpy as np


# Main script
def main():
    # First we add arguments (--file for naming the file, --row for n rows, --column for n columns)
    parser = argparse.ArgumentParser(description="Creates an empty .csv of dimensions specified by user")
    parser.add_argument('-f', '--file', required=True, help='<file_name>.csv')        
    parser.add_argument('-c', '--column', type=int, required=True, help='x columns')
    parser.add_argument('-r', '--row', type=int, required=True, help='y rows')
    parser.add_argument('--d', '--delimiter', default=',', help='Specify delimiter, set to comma by default')
    parser.add_argument('-dir', '--directory', default=os.getcwd(), help='Set output directory') # Later, create default output dir in cwd  
    args = parser.parse_args()

    print(args)