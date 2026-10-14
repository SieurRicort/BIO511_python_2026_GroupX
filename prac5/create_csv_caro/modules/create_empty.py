#!/usr/bin/env python3
import numpy as np
import csv
import os
import numpy as np


def empty_csv(file_name, _x, _y, ):
    csv_output = os.path.join(os.path, file_name)
    with open(csv_output, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(_x):
            if _x > 0:
                writer.writerows(i['']*_y)
    return csv_output

#def new_empty_csv():
#    with open(new_file. 'W')





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











