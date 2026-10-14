#!/usr/bin/env python3
# Calls on create_empty.py and converts array to .csv


from modules.create_empty  import empty_csv
import argparse
import os 



# Main script
def main():
    # First we add arguments (--file for naming the file, --row for n rows, --column for n columns)
    parser = argparse.ArgumentParser(description="Creates an empty .csv of dimensions specified by user")
    parser.add_argument('-f', '-file', required=True, help='<file_name>.csv')        
    parser.add_argument('-c', '-column', type=int, required=True, help='Specify number of columns')
    parser.add_argument('-r', '-row', type=int, required=True, help='Specify number of rows')
    #parser.add_argument('--d', '--delimiter', default=',', help='Specify delimiter, set to comma by default') # Necessary?
    parser.add_argument('-o', '--output', default=os.getcwd(), help='Specify output directory if other than ./') # Later, create default output dir in cwd  
    #parser.add_argument('-d', '--dtype', default=None, help='Set limit to allowed data types in file') #default=str,
    args = parser.parse_args()  
    print(args)

    # Validates row and column inputs
  #  if args.row <= 0 or args.column <= 0:
  #      parser.error("Wrong input: Row and column need to be set at 1 or more.")
    # Validated file name input
  #  if '.csv' not in args.file:
  #      a, b = args.file(), '.csv'
  #      args.file() == a + b
#    if not args.file.endswith('.csv'):
#        args.f = parser.
#        parser.error("Wrong input: the file name should end with '.csv'.")
    # Validates output directory
    if not os.path.isdir(args.output):
        parser.error(f"Output directory does not exist or is not a directory: {args.output}")

        # Call the function to create the file 
        pew = empty_csv(args.file, args.column, args.row, args.delimiter)




if __name__ == '__main__':
    main()
    print(main)

        