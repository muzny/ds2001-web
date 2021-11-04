#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felix Muzny
DS 2001 - CS
September 22/23, 2021 
Practicum 3 - "Slides"!
"""

# import a library of functions that we
# can later use
# there are many other libraries available
# built-in: random, math, etc.
# we can install: matplotlib
import random

def main():
    print("'Slides' for practicum 3")
    # warm up: which of the 
    # following function calls 
    # is best for simulating rolling
    # a die?
    
    ## A - doesn't save the return value
    # random.randint(1, 6)
    ## B - best!
    roll = random.randint(1, 6)
    ## C - doesn't save the return value AND function isn't called properly
    # randint(1, 6)
    ## D - function isn't called appropriately
    #roll = randint(1, 6)
    print("roll:", roll)
    
    # Boolean Values!
    # What do we remember?
    # True or False
    # must capitalize the T and the F
    # can save them in variables
    # datatype just like int, but with only 2 options
    likes_cats = True
    print(likes_cats)
    print(type(likes_cats))

    # Boolean Expressions
    # any expression that evaluates to a 
    # boolean value
    print("greater than 3?", roll > 3)
    # use two equals
    print("is exactly 3?", roll == 3)
    print("is not 3?", roll != 3)
    
    # two boolean -> one boolean
    print("and1:", True and True)  # True
    print("and2:", True and False)  # False
    print("and3:", False and False) # False
    print("False == False:", False == False) # True
    
    
    print("test1:", roll > 2 and roll < 5)
    
    # what is our order of operations?
    # math first
    # then comparison (<, >, ==)
    # then we do "and", "or"
    
    
    print("or1:", True or True)    # True
    print("or2:", True or False)   # True
    print("or3:", False or False)  # False
    # True when roll is not  4, 2, 5
    print("test2:", roll < 2 or roll > 5 or roll == 3) 
    
    # When is the following True? 
    # True ALWAYS
    print("test3:", roll > 2 or roll < 5)  
    
    # Recommendation: 
    # Play around a little with the boolean 
    # casting function - bool()
    print(bool(3))
    
    
    # Conditionals
    print()
    print()
    print("roll:", roll)
    print("conditional:")
    
    # Task:
    # Want to print "prime!" if the user
    # rolls a 2, 3, or 5
    if roll == 2 or roll == 3 or roll == 5:
        print("prime!")
        
    # Make sure to not write this conditional as:
    if roll == 2 or 3 or 5:
        print("prime!")
    # This is because python will interpret it as:
    # if roll == 2 or bool(3) or bool(5):
    # and bool(3) and bool(5) are ALWAYS True!
    
    
    # Not done in class, but think about this:
    # What happens when we 
    # run the following
    # code?
    
    # x = -8
    # if x < 0:
    #     print("tiny")
    # if x < 100:
    #     print("middling")
    # else:
    #     print("greater than 100")
        
        
    # Reading files
    # Remember: put the files that you want to read
    # in the __same__ directory/folder as your code!
    
    # Step 1: open the file, in read mode

    
    # step 1 - open the file
    file = open("allston.txt", "r")
    # step 2 - read its contents
    line = file.readline()
    print(line)
    print(type(line)) # string!
    # step 3 - close the file
    file.close()
    
    # step 1
    # if your data is in the folder called
    # neighborhood_data
    file = open("neighborhood_data/allston.txt", "r")
    # step 2
    line = file.readline()
    print(line)
    # step 3
    file.close()
    
    
    # Now we have our data that we can play around with!
    # What type is it?
    
    # Answer: we ALWAYS read in data from files as strings
    
main()

