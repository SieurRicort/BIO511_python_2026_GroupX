import argparse

parser = argparse.ArgumentParser(description="Read a CSV file and print a statistical summary.")
parser.add_argument("csv_file", help="Path to the CSV file to read")
args = parser.parse_args()

print("The file I received is:", args.csv_file)

import argparse
import csv

parser = argparse.ArgumentParser(description="Read a CSV file and print a statistical summary.")
parser.add_argument("csv_file", help="Path to the CSV file to read")
args = parser.parse_args()

rows = []
with open(args.csv_file) as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

print(rows)




import argparse
import csv
import pandas as pd

parser = argparse.ArgumentParser(description="Read a CSV file and print a statistical summary.")
parser.add_argument("csv_file", help="Path to the CSV file to read")
args = parser.parse_args()

rows = []
with open(args.csv_file) as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

df = pd.DataFrame(rows).astype(float)

print(df)
print(df.describe())