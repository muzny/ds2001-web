"""
Utility functions to be used in DS 2001 - Computer Science practicum
Practicum 6

import with the code:
import p6_utils
"""

def file_to_list(filename):
    """
    name: file_to_list
    This function takes a file path and reads the file, returning the contents of
    the file as a list of strings. Any newline characters are removed.
    parameters:
    filename - str the path to the file to read
    return:
    list of strings, where every element in the list is one line from the file
    """
    ls = []
    file = open(filename, "r")
    line = file.readline()
    while line != "":
        ls.append(line.strip())
        line = file.readline()
    file.close()
    return ls

def main():
    print("p6_utils main!") 

if __name__ == "__main__":
    main()
    
    
    







