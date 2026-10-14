#!/usr/bin/env python3
import numpy as np


# Thought; create empty 5x5 array and convert to .csv?
# https://www.geeksforgeeks.org/python/convert-numpy-array-into-csv-file/

#  name, columns, rows, data type, 
def empty_array(new_name, x, y, type):
    shape = (x, y)
    dtype=type
# (x, y), data type, Column major, like??
    test_array = np.empty(shape, dtype=type, order='C', like=None)
    return empty_array

#







def array_csv(file_name, array, delimiter):
    with open(empty_array, mode='x', ) as csv_file: 




