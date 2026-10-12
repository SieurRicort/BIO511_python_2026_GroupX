#!/usr/bin/env python3

# Import modules
from Bio import SeqIO
import argparse
import csv


def build_parser():
    parser = argparse.ArgumentParser(description="Read a FASTA file and print sequence summaries.")
    parser.add_argument("-f", "--file", required=True, help="Input FASTA file")
    parser.add_argument("-o", "--output", required=True, help="Output file as a csv")
    return parser

def load_report(file, output):
    """
    Read FASTA records and print their ID, length, and first 10 bases.
    Return a list of SeqRecord objects.
    """
    records = list(SeqIO.parse(file, "fasta")) # List of SeqRecord objects from input file

    with open(output, mode="w", newline='') as csvfile:
        writer=csv.writer(csvfile, delimiter='\t') # Create a csv file with tab delimiter
        writer.writerow(["ID", "Length", "First nucleotides"]) # Sets the header as ID Legnth First nucleotides

        for record in records: # Loops through SeqRecords
            writer.writerow([record.id, len(record.seq), record.seq[:10]]) # Creates a new row with seq.id, len(seq), 10 first nt of seq
        return records


def main():
    parser = build_parser()
    args = parser.parse_args()

    output = load_report(args.file, args.output)

if __name__ == "__main__":
    main()