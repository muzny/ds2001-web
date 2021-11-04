"""
Utility functions to be used in DS 2001 - Computer Science practicum

import with the code:
import kmeans_utils as utils

note that the "as utils" is not required, but will make you need to type less! :)
"""
import random

def generate_points(number, minimum = 0, maximum = 10):
    """
    name: generate_points
    This function generates a list of 2-d points
    where each point's coordinates are between minimum and maximum.
    Parameters:
    number - integer indicating how many points to generate
    minimum - integer indicating minimum (inclusive) value to generate. Default value 0.
    maximum - integer indicating maximum (inclusive) value to generate. Default value 10.
    return:
    list of tuples with the given number of points
    """
    return [(random.randint(minimum, maximum), random.randint(minimum, maximum)) for i in range(number)]

def get_column(data, index):
    """
    name: get_column
    This function takes a list of lists and an integer and
    gives the user the list of values from the indicated column.
    Does not change the passed in list of lists.
    Parameters:
    data - list of lists
    index - integer indicating which column values to access
    return:
    List of values where the first value is the value at position "index" from the 
    first row in data, the second value is the value at position "index"
    from the second row in data, etc for all rows in data
    """
    column = []
    for row in data:
        column.append(row[index])
    return column
