#!/usr/bin/env python3

# Import modules
from Bio.SeqRecord import SeqRecord # Imports SeqRecord class
from Bio import SeqIO # Imports SeqIO module
import argparse

# Arg parser to use while executing the script
def build_parser():
    parser = argparse.ArgumentParser(description="Read a FASTA file and print sequence summaries.")
    parser.add_argument("-f", "--file", required=True, help="Input FASTA file")
    return parser

# Reverse seq function
def reverse_seq(file):
    """
    Read FASTA records, reverse the sequence and store them in a new fasta file.
    """
    records = list(SeqIO.parse(file, "fasta")) # List of SeqRecord objects from input file
    reverse_records=[] # Empty list
    for record in records: # Loops through SeqRecord
        forward = record.seq # Gets the sequence
        reverse=forward.reverse_complement() # Gets the reverse_completement
        reverse_record=SeqRecord( # Creates a SeqRecord for the reverse_complement
            seq=reverse,
            id=f"{record.id}_rc",
            description=f"reverse completement of {record.id}"
        )
        reverse_records.append(reverse_record) # Adds the SeqRecord in the output list
        SeqIO.write(reverse_records, "dna_rc.fasta", "fasta") # Appends that list as an entry for a fasta file
    return reverse_records

def main():
    parser = build_parser()
    args = parser.parse_args()

    reverse_seq(args.file)

if __name__ == "__main__":
    main()