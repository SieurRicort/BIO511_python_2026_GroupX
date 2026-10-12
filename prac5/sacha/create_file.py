#!/home/sacha/miniconda3/envs/Fasta/bin/python3

# Import modules
import os
import csv

def create_csv(wd, csv_name, row, column, delim):

    # Where will be the new csv
    csv_file_path=os.path.join(wd, csv_name)

    # Create the csv file
    try:
        with open(csv_file_path, mode='x', newline='') as file:
            writer = csv.writer(file, delimiter=delim) # creates as many rows as we input using , as a delimiter

            for _ in range(row):
                writer.writerow([''] * column) # creates as many columns as we input with nothing in it

    except FileExistsError: # handles error if file already existing
        print(f"Error: {csv_name} already exists.")
        return None

    return csv_file_path