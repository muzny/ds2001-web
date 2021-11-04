"""
Felix Muzny
October 13th/14th, 2021
DS 2001 - CS Practicum #6

A program to read names and jobs, perform some analysis,
and display some interesting information!
"""


import p6_utils

def same_length(lst1, lst2):
    """
    name: same_length
    This function takes two lists and verifies that they have the same number of elements.
    parameters:
    lst1 - first list
    lst2 - second list
    return:
    True if both lists have the same length, False otherwise
    """
    return len(lst1) == len(lst2)

def pretty_print(lst1, lst2):
    """
    name: pretty_print
    This function takes two lists and prints out the elements in the following format:
    lst1_value1: lst2_value1
    lst1_value2: lst2_value2
    lst1_value3: lst2_value3
    ...
    For all items in the list
    parameters:
    lst1 - first list
    lst2 - second list
    return:
    none
    """
    for i in range(len(lst1)):
        print(lst1[i] + ": " + lst2[i])


def lookup_by_name(names, begins_with):
    """
    name: lookup_by_name
    This function takes a list of names and a string and returns a new list of all the names 
    that begin with the supplied string. Case insensitive.
    parameters:
    names - list of names
    begins_with - string to search for
    return:
    a new list of names from the original names list that begin with the begins_with string
    """
    ls = []
    for name in names:
        if name.lower().startswith(begins_with.lower()):
            ls.append(name)
    return ls

def count_matches(ls, to_count):
    """
    name: count_matches
    This function takes a list of values and a target value and counts the number of times
    the target value appears in the list of values.
    parameters:
    ls - list of elements
    to_count - value to search the list for
    return:
    integer number of times to_count appears in ls
    """
    total = 0
    for val in ls:
        if val == to_count:
            total += 1
    return total


def main():
    names = p6_utils.file_to_list("names.txt")
    jobs = p6_utils.file_to_list("jobs.txt")
    print(names[:3])
    print(jobs[:3])
    if not same_length(names, jobs):
        print("they don't match! :(")
        print(len(names))
        print(len(jobs))
    else:
        print("congrats, they match in length!")
        print()
        pretty_print(names, jobs)
        print()
        begin_with_a = lookup_by_name(names, "A")
        print("Names beginning with 'A'")
        print(begin_with_a)
        begin_with_ann = lookup_by_name(names, "ANN")
        print("Names beginning with 'ANN'")
        print(begin_with_ann)
        print()
        matches = count_matches(jobs, "MINER")
        print("jobs that are MINER:", matches)
        
    # Since Task 6 was a "bonus", we haven't included the code here
    # feel free to stop by office hours if you implemented it and 
    # want to check out your answers!

main()
