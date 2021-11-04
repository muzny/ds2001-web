"""
Utility functions to be used in DS 2001 - Computer Science practicum
Practicum 7

import with the code:
import p7_utils
"""

import csv

def read_csv(filename):
    ''' Function: read_file
        Parameters: a string, the name of the file we're reading
        Returns: a list of lists of strings, all the data we read
    '''
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # skip the header line
        for row in reader:
            data.append(row)
    return data
