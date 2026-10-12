#!/usr/bin/env python3

"""Load the row data for the CSV from one of three sources: an inline
JSON string, a .json file, or a plain delimited text file. Each loader
returns a plain list of lists; structural validation happens separately
in main.py (validate_data), not here.
"""
 
import json
import csv
 
 
def load_from_json_string(json_str):
    """Parse an inline JSON string, e.g. '[[1, 2], [3, 4]]'."""
    return json.loads(json_str)
 
 
def load_from_json_file(file_path):
    """Read a .json file containing a list of lists."""
    with open(file_path, mode='r') as file:
        return json.load(file)
 
 
def load_from_text_file(file_path):
    """Read a delimited text file, detecting its input delimiter."""
    with open(file_path, mode="r", newline="") as file:
        sample = file.read(4096)
        file.seek(0)

        try:
            dialect = csv.Sniffer().sniff(
                sample,
                delimiters=",;\t|"
            )
            reader = csv.reader(file, dialect)
        except csv.Error:
            reader = csv.reader(file, delimiter=",")

        return list(reader)
 
 
def load_data(args):
    if args.data is not None:
        return load_from_json_string(args.data)

    if args.data_file.endswith('.json'):
        return load_from_json_file(args.data_file)

    return load_from_text_file(args.data_file)
