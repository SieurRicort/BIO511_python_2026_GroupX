#!/usr/bin/env python3

"""Load a CSV file, print summary statistics, and save them."""

import csv
import pandas as pd
import os


def get_stats(file_path, delim):
    """Calculate descriptive statistics and save them to a CSV file."""

    try:
        with open(file_path, mode="r", newline="") as file:
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
    df = df.apply(pd.to_numeric, errors="coerce")

    print("\nDataFrame:")
    print(df)

    if df.empty or df.shape[1] == 0:
        print("No data available for statistical analysis.")
        return None

    summary = df.describe().round(1)

    print("\nStatistical summary:")
    print(summary)

    # Create the summary filename next to the original CSV
    base, _ = os.path.splitext(file_path)
    summary_path = base + "_summary.csv"

    try:
        summary.to_csv(summary_path, sep=delim)
        print(f"\nSummary saved to: {summary_path}")

    except OSError as e:
        print(f"Error: could not save summary: {e}")
        return summary

    return summary

# input_file = str('/home/sacha/GITHUB/BIO511_python_2026_GroupX/prac5/sacha/output.csv')
# get_stats(input_file, ',')