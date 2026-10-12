#!/usr/bin/env python3

# Import modules
from Bio import SeqIO # Imports SeqIO module
from Bio.SeqUtils import gc_fraction
import argparse
import csv

# Arg parser to use while executing the script
def build_parser():
    parser = argparse.ArgumentParser(description="Read a FASTA file and print sequence summaries.")
    parser.add_argument("-f", "--file", required=True, help="Input FASTA file")
    parser.add_argument("-o", "--output", required=True, help="output csv file")
    return parser

# Reverse seq function
def GC_content(file, output):
    """
    Read FASTA records, calculate GC content and save it in a csv file along with sequence IDs.
    """
    records = list(SeqIO.parse(file, "fasta")) # List of SeqRecord objects from input file
    with open(output, mode="w", newline='') as csvfile:
            writer=csv.writer(csvfile, delimiter='\t') # Create a csv file with tab delimiter
            writer.writerow(["ID", "GC content (%)"]) # Sets the header as ID Legnth First nucleotides
    
            for record in records: # Loops through SeqRecords
                writer.writerow([record.id, 100*gc_fraction(record.seq)]) # Creates a new row with seq.id and GC content
            return records

def main():
    parser = build_parser()
    args = parser.parse_args()

    GC_content(args.file, args.output)

if __name__ == "__main__":
    main()