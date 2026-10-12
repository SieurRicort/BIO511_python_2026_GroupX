#!/usr/bin/env python3

"""
Build a CSV from JSON or text input, then print its summary statistics.

How to use this command:

1. Create a CSV file from inline JSON data:
   python3 main.py -f output.csv -df '[[1,2,3],[4,5,6]]'

2. Create a CSV file from a JSON file:
   python3 main.py -f output.csv -ff data.json

3. Create a CSV file from a delimited text file:
   python3 main.py -f output.csv -ff data.txt -del ','

4. Specify the output directory:
   python3 main.py -f output.csv -df '[[1,2],[3,4]]' -dir ./results

5. Use tab delimiter
   python3 main.py -f output.csv -ff data.txt -del $'\t'

"""

from create_file import create_csv
from summary_stats import get_stats
from data_loader import load_data

import argparse
import os
import json
import sys


def build_parser():
    parser = argparse.ArgumentParser(description="Create a CSV file from JSON or text data, then print summary statistics.")
    parser.add_argument('-f', '--file', required=True, help='Name of the file to create (must end with .csv)')
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('-df', '--data', help='Row data as an inline JSON string, e.g. "[[1,2],[3,4]]"')
    source.add_argument('-ff', '--data-file', help='Path to a .json file, or a delimited .txt file with the rows')

    parser.add_argument('-del', '--delimiter', choices=[',', ';', '\t', '|'], default=',', help='Delimiter for the output CSV (default: comma)')
    parser.add_argument('-dir', '--directory', default=os.getcwd(), help='Existing output directory (default: current working directory)')
    return parser


def validate_args(args, parser):
    if not args.file.endswith('.csv'):
        parser.error("Wrong input: the file name should end with '.csv'.")

    if not os.path.isdir(args.directory):
        parser.error(f"Output directory does not exist or is not a directory: {args.directory}")

    if args.data_file is not None and not os.path.isfile(args.data_file):
        parser.error(f"Input data file not found: {args.data_file}")


def validate_data(data, parser):
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        parser.error("Data must be a list of lists, e.g. [[1, 2], [3, 4]].")

    if data and any(len(row) != len(data[0]) for row in data):
        parser.error("All rows must have the same number of elements.")


def main():
    parser = build_parser()
    args = parser.parse_args()
    validate_args(args, parser)

    try:
        data = load_data(args)
    except json.JSONDecodeError:
        parser.error("Invalid JSON data.")
    except OSError as e:
        parser.error(f"Could not read input data: {e}")

    validate_data(data, parser)

    csv_path = create_csv(args.directory, args.file, data, args.delimiter)
    if csv_path is None:
        sys.exit(1)

    get_stats(csv_path, args.delimiter)

if __name__ == '__main__':
    main()