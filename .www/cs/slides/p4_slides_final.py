#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Felix Muzny
DS 2001 - CS
Sept 29 & 30, 2021 
Practicum 4 - "Slides"!
"""

# While you wait:
# 1) Look at the feedback from your p3 submission (on Gradescope)
#       (you might not have any feedback, this would be in line)
#       (with your code or on the right side by the rubric)
# 2) Compare and constrast Tasks 1 & 2 from our solution
# with your solution.
# (our solution is on the course website, next to the materials
# from last week)
#
# If you did not construct the filename from the user input,
# pay special attention to the Task 1 solution!
#
#
#

# Data discussion will be uploaded separately after the 
# students who need to make up this work have finished!

import random 

# 2) While loops: what do we remember?
# for repeating code
# it will iterate (repeat) until it reaches the stopping point
# the stopping point is when the condition becomes False
# "while" then a condition (boolean expression), then ":"
# if we write "while True:", then we'll need a "break" to 

# 3) write a program for a mini guessing game
# the game is the following:
# I think of a number
# you guess a number
# if you get the number correct, we stop
def main():
    secret_number = random.randint(0, 10)
    # print out the secret number so that 
    # we can debug our code
    print("secret number: ", secret_number)
    print()
    
    # a few different options for this code
    # Option 1
    guess = int(input("guess? "))
    guesses = [guess]
    while guess != secret_number:
        guess = int(input("guess again? "))
        guesses.append(guess)
        
    print("you won!")
    print(guesses)
        
    # a few different options for this code
    # Option 2
    guess = -1 # a "dummy" value just to get the loop started
    guesses = []
    while guess != secret_number:
        guess = int(input("guess? "))
        guesses.append(guess)
    
    # at this point this is guaranteed
    # guess == secret_number
    print("you won!")
    print(guesses)
    
    
    # a few different options for this code
    # Option 3
    guess = int(input("guess? "))
    guesses = []
    while guess != secret_number:
        guesses.append(guess)  # add the guess in *first*
        guess = int(input("guess? "))
        
    # remember to append the final guess
    guesses.append(guess)
    
    # at this point this is guaranteed
    # guess == secret_number
    print("you won!")
    print(guesses)
    
main()


