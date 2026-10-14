#!/usr/bin/env python3
from premade_script import codons, exercise_function    
import argparse
import os
import Bio
from Bio import *


#	 Call on in terminal;   
# python3 main.py -s <seq file>



def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Split the sequences in a FASTA file into codons.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file') # Whyyyyy -s? 
    args = parser.parse_args()





    
    # We first call the function from the script, and use the input file path as an argument
    sequence_codons = codons(args.sequence)
    
    # Here you need to check the output of the function
    print(sequence_codons)
    
    # Here you need to call the exercise_function from premade_script.py
    aa_string = exercise_function(sequence_codons)
    print(aa_string)
    # And check the output of that function
if __name__ == "__main__":
    main()
