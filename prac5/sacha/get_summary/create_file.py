#!/home/sacha/miniconda3/envs/Fasta/bin/python3

"""Create a CSV file from a list of rows."""
 
import os
import csv
 
 
def create_csv(wd, csv_name, data, delim):
    """Write data (a list of lists) to a new CSV file in wd.
 
    Returns the file path on success, or None if the file already
    exists or cannot be created. Can be called directly with a
    Python list object -- it does not depend on the CLI or data_loader.
    """
    csv_file_path = os.path.join(wd, csv_name)
 
    try:
        with open(csv_file_path, mode="x", newline="") as file:
            writer = csv.writer(file, delimiter=delim)
            writer.writerows(data)
    except FileExistsError:
        print(f"Error: {csv_name} already exists.")
        return None
    except OSError as e:
        print(f"Error: could not create {csv_name}: {e}")
        return None
 
    return csv_file_path
