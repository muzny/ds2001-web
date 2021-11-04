#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Felix Muzny
DS 2001 - CS
October 20th/21st, 2021 
Practicum 7 - "Slides"!
"""

# Due dates this week:
# Friday @ 12pm (noon) — P7
#
# Friday @ 9pm (at night) - Final Group projects + topics
# you should be able to finish this in class today
# (in general, your final project deadlines will be at 9pm)

"""
Final Project:

0) Questions?
    
    
1) If you are looking for a group/teammate and don't have one yet:
    a) Look on the Canvas discussion for teammates, see if 
    one of the projects matches your interests/work schedule well!
"""

# any imports here


# define any constants here


# no other variables should "live"
# outside of functions or "if __name__ == "__main__":"!

# When we structure our programs, we have the functions that 
# we've defined at the top, and *one* "if __name__ == "__main__":"
# at the bottom

# functions that we wrote for practicum last time!
# (if you didn't finish these, feel free to download
# the solutions from canvas)

def same_length(lst1, lst2):
    """
    name: same_length
    This function takes two lists and verifies that they have 
    the same number of elements.
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
    This function takes two lists and prints out the 
    elements in the following format:
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

"""
Group questions from last time that we're going to discuss now:
1) What _types_ can we pass as parameters to 
    the same_length function?

2) What does a function return when it has no
    return statement (like in pretty_print)?
    
"""

if __name__ == "__main__":
    print("p7 slides!")
    print()
    
    nums = ["1", "2", "3"]
    lets = ["a", "b", "c"]
    
    # What happens if a function has multiple
    # return statements? What if a return statement
    # is inside of a loop?
    big_nums = [1000, 238, 2000, 70000, -2346]
    
    
    # Two dimensional lists as tables of data!
    # [["row 1", "row 1 col 2"],
    #  ["row 2", "row 2 col 2"],
    #  ["row 3", "row 3 col 2"]]
    
    # read in the tiny data using the p7_utils module
    
    
    # indexing into two dimensional lists
    
    
    # For p7, you're aiming to finish task 2
    # hint: you only need one loop
    
    
    

