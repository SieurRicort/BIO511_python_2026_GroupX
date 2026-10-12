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
def translate_seq(file):
    """
    Read FASTA records, translate it into proteins (print first 10 amino acids)
    """
    records = list(SeqIO.parse(file, "fasta")) # List of SeqRecord objects from input file
    aa_records=[]

    for record in records:
        dna_seq=record.seq
        aa_seq= dna_seq.translate()
        aa_record=SeqRecord( # Creates a SeqRecord for the reverse_complement
            seq=aa_seq,
            id=record.id,
            description=f"translation of {record.id} in amino acids."
        )
        aa_records.append(aa_record) # Adds the SeqRecord in the output list
    SeqIO.write(aa_records, "amino_acids.fasta", "fasta") # Appends that list as an entry for a fasta file
    return aa_records

def main():
    parser = build_parser()
    args = parser.parse_args()

    translate_seq(args.file)

if __name__ == "__main__":
    main()