#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Felix Muzny
DS 2001 - CS
October 6/7, 2021 
Practicum 5 - "Slides"!
"""

"""
Logistics notes:    
    - This week, we **will** have a small amount of 
    homework to complete before practicum next week
"""

"""
Warm-up:

Write the equivalent __while__ loop to the following for loop:
(Go ahead and do this in your p5.py file, you can leave it there
 in comments or not)
"""    
ls = ["a", "b", "c", "d"]
print("loop 1")
# range is going to produce [0, ...., len(ls) - 1]
# so that the variable i can go from 0 to len(ls) - 1 
for i in range(len(ls)):
    print(ls[i])
print()

count = 0
while count < len(ls):
    print(ls[count])
    count += 1
    # if you printed out ls[count] here instead, you'd get
    # an error because you run off the end of the list!

#Write the equivalent __while__ loop to the following for loop: 
# start (inclusive), stop (exclusive), increment
# [0, 2, 4, .... len(ls) - 1]
print("loop 2")
for i in range(0, len(ls), 2):
    print(ls[i])
    
print()

count = 0
while count < len(ls):
    print(ls[count])
    count += 2


print("loop 3")
#Write the equivalent __while__ loop to the following for loop:   
# letter takes the next __value__ in the list (rather than the position)
for letter in ls:
    print(letter)  
    #print(ls[letter]) # ERROR
    
print()

count = 0
while count < len(ls):
    letter = ls[count]
    print(letter)
    count += 1


"""
(links for this discussion are on the course website)

 1) Playing with ELIZA
http://psych.fullerton.edu/mbirnbaum/psych101/Eliza.htm

What is one thing that your group found that 
ELIZA is unable to do?

 
"""

# Programming review topics for the day:
# string manipulation
# list manipulation & looping


# 2) demo some string manipulation
def main():    
    print()
    print("p5 slides")
    # String manipulation
    
    # Strings are immutable
    color = "purple"
    print(color[len(color) - 1])
    print(len(color))
    #color[0] = "b"  # ERROR
    color = "burple"

    # upper()
    color = color.upper()
    print(color)
    #print(upper_color)
    # lower()
    # strip()
    print()
    
    # Lists are mutable
    # Change a string list element into the upper case version
    animals = ["dog", "cat", "wombat", "panther", "ocelot"]
    print(animals)
    animals[0] = "ferret"
    print(animals)
    animals[0] = animals[0].upper()
    print(animals)
    
    
    # change all the elements in the list into the 
    # upper case versions
    for i in range(len(animals)):
        print(animals[i])
        animals[i] = animals[i].upper()
        
    print(animals)
    
    # while loop version
    index = 0
    while index < len(animals):
        animals[index] = animals[index].upper()
    
    # list slicing - gives you a sublist
    # start:stop (stop is exclusive)
    print(animals[1:4])
    
    
main()