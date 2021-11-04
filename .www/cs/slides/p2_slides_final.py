#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felix Muzny
DS 2001 - CS
Sept 15/16, 2021
Practicum 2 - "Slides" (final version)!
"""

# Pre-warm-up:
# introduce yourself to your neighbor
# what is your favorite breakfast food?


# Warm-up:
# Which of the following are valid variable declaraions?
my_best_variable_life = "I love DS 2000!"
name = "Jordan"
# "Jordan" = name  # won't work because the variable name MUST be on the left!
age = 40
age_in_seven_years = age + 7
band_3oh3 = "it's a band!"

# What do we remember about variables?
# variable_name = value
# the ONLY thing on the left hand side of the = sign is the variable name!!!
#
# what kind of values can we have?
# numbers - float (3.2, decimal), integers (3, 5, -3)
# strings - "sequence of letters in quotes"
# boolean - leave this for next week



# What is the difference between the following lines of code?
name = "Avatar Korra"
print("name")  # the string "name"
print(name)    # value of the variable name

# Updating variables:
# trace the value of x in the following code
x = 4       # create the variable x, set it to 4
y = 13      # create the variable y, set it to 13
print(x)
x = y       # variable x gets the value of y (13)
print(x)
x = x + 1   # gets the old value of x, add 1, update the value of x
print(x)
# what is the value of y here?
# 13. no place where y is on the left in the code above, so it
print(y)    
# what if we use the variable explorer and the debugger?
# For variable explorer: go to "view" -> Panes -> Variable Explorer
# For debugger:
# click on the left of a line between the line and line number to
# get a red "breakpoint", then press the blue "debug file" button.
# (looks like an arrow and a pause sign), then the run current
# line button to step through the code.

# arithmetic with strings????
# print(3 + 4)
# called "string concatenation" -> glue two strings together
print("cat" + "dog")   # works! 
#print("cat" - "dog")

# What is a function?
# a "mini-program" that does a certain
# set of steps to accomplish some job
# function_name(arguments)
print("hi")
# for functions with return values
# variable_name = function_name(arguments)
name = input("name?")  # returns what the user entered
print(type(name))

# Casting (changing datatypes) & return values
# if a function returns a value and you do not save
# it in a variable, it is LOST FOREVER
number = "123"
number = int(number)
print(type(number))

# the input() function
# does this function have a return type?
# ALWAYS returns a string


# How do I stop a program in spyder?
# use the red square to the upper right of the console
# OR x-out of the console on the left part of the console tab

# the help() function
help(print)