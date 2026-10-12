#!/home/sacha/miniconda3/envs/Fasta/bin/python3

# Import functions
from create_file import create_csv

#Import modules
import argparse
import os

# Main script
def main():
    # First we add arguments (--file for naming the file, --row for n rows, --column for n columns)
    parser = argparse.ArgumentParser(description="Create a csv file with multiple arguments (file name, delimiter, row, column) to the working directory")
    parser.add_argument('-f' , '--file', required=True, help='Name file you want to create (must end with .csv)')
    parser.add_argument('-r', '--row', type=int, required=True, help='Input how many rows')
    parser.add_argument('-c', '--column', type=int, required=True, help='Input how many columns')
    parser.add_argument('-delim', '--delimiter', choices=[',', ';', '\t', '|'], default=',', help='delimiter for the .csv file. default is comma')
    parser.add_argument('-dir', '--directory', default=os.getcwd(), help='Existing output directory (default: current working directory)')
    args= parser.parse_args()

    # Validates row and column inputs
    if args.row <= 0 or args.column <= 0:
        parser.error("Wrong input: Row and column need to be set at 1 or more.")
    # Validated file name input
    if not args.file.endswith('.csv'):
        parser.error("Wrong input: the file name should end with '.csv'.")
    # Validates output directory
    if not os.path.isdir(args.directory):
        parser.error(f"Output directory does not exist or is not a directory: {args.directory}")

    
    # Call the function to create the file
    result = create_csv(args.directory, args.file, args.row, args.column, args.delimiter)

    if result is not None:
        print(f"{args.file} successfully created in {args.directory}.")

if __name__ == '__main__':
    main()