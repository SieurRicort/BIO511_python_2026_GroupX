#!/usr/bin/env python3
from fasta_to_codon import codons
import argparse
import os


def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Split the sequences in a FASTA file into codons.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file')
    args = parser.parse_args()
    
    # We first call the function from the script, and use the input file path as an argument
    sequence_codons = codons(args.sequence)
    
    # Here you need to check the output of the function
    print(sequence_codons) # A dictionnary

    # Here you need to call the exercise_function from fasta_to_codon.py
    from fasta_to_codon import exercise_function # import the function
    for header, codon_list in sequence_codons.items(): # Goes through the dictionnary
        exercise_function(codon_list) # Calls the command for every codon list
        print(header, exercise_function(codon_list)) # And check the output of that function (protein)
if __name__ == "__main__":
    main()