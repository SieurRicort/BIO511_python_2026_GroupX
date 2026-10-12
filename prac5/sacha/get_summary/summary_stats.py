#!/usr/bin/env python3

"""Load a CSV file into a DataFrame and print its summary statistics."""
 
import csv
import pandas as pd
import os
 
def get_stats(file_path, delim):
    """Read file_path as a delimited CSV, print it and its describe()
    table, and return the resulting DataFrame. Non-numeric cells become
    NaN (pd.to_numeric errors='coerce') rather than raising.
    """
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=delim)
            data = list(reader)
    except OSError as e:
        print(f"Error: could not read {file_path}: {e}")
        return None
 
    if not data:
        print("The CSV file is empty. No statistics to calculate.")
        return None
 
    headers, rows = data[0], data[1:]
    df = pd.DataFrame(rows, columns=headers)
    df = df.apply(pd.to_numeric, errors='coerce')
 
    print("\nDataFrame:")
    print(df)
 
    print("\nStatistical summary:")
    print(df.describe())
 
    return df

# input_file = str('/home/sacha/GITHUB/BIO511_python_2026_GroupX/prac5/sacha/output.csv')
# get_stats(input_file, ',')