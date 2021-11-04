#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Felix Muzny
DS 2001 - CS
October 13/14, 2021 
Practicum 6 - "Slides"!
"""
    
"""
(if you didn't read the final project description,
go do this __now__!)

Final Project:

1) What do you think makes a given data set 
    compelling to work with?
    - well organized
    - if we can see trends/correlations
        (be able to investigate the correlations 
         that we're interested in)
    - all the data is about some central theme/topic
    - has a lot of data points
    - both qualitative and quantitiave data
    - over a time span
    - topics that are recent (timely & relevant)
    - variation in the data 
    - __interesting__ (topic that you care about)
    - relevant to what you are interested in/our lives
    - organized/clean/nice structure
    - variation (shows interesting patterns, correlations)
    - it makes you think about external connections/new questions
    - data from a reliable source/not biased
    - comprehensive
    - insights that aren't otherwise obvious

    
In groups, briefly discuss:
    0) Take a look at the list of example projects from
    semesters past for inspiration (on the course website)

    
    1a) what dataset did you find and why might 
    it be interesting to work with
    
    
    1b) Look at the data set discussion thread on Canvas.
    What's one interesting data set that someone else found
    that you might be interested in?
    
    
    2) does your group have any questions about the final project?
        a) if yes, post your question on the pinned
        Canvas discussion thread for final project questions
        
Final project logistics:
    - data formats?
        - there will be different formats, some easier to read 
        (as a human & as a computer than others)
        - if you find a dataset in a format you are unfamiliar with,
        reach out to us-we are here to help!
            
    - first deadline: next Friday (October 22nd)
        - what is your topic (broadly), who is in your group (1 - 3 people)
    
"""

# what is a function?
# start with def function_name(parameters)
# parameters act as input to the function
# return value is going to be the functions output
# defining functions helps us re-use code 
# it makes our code modular
# so that we build our programs out of blocks that can 
# be re-used and applied to new but similar contexts

"""
Warm-up #2:
    
pull up either your p5.py code or download 
and pull up the p5_task3.py that is posted for you
on the course website (under the week's materials for Practicum 5)
 
"""

# Programming review topics for the day:
# functions + scope


# importing another python file as a module
import p6_utils
# the p6_utils.py file needs to be in the same folder
# return_value = p6_utils.function_name(parameters)

# program structure:
# we always put our other function definitions 
# before our definition of main()

# when you define a function, you __must__ put
# a line of code inside it for it to not throw an error!
def example_function():
    print("here's a line of code")
    
def subtract(a, b):
    # a = first value passed in
    # b = second value passed in
    
    # a and b only "live" inside this function
    answer = a - b
    
    # return the value of the answer variable
    return answer

def main():
    print("p6 slides!")
    print()
    
    # example calling the p6_utils file_to_list function
    #names = p6_utils.file_to_list("names.txt")
    #print(names)
    
    # example call to subtract, passing in raw values
    result = subtract(10, 6)
    print("first result of subtract:", result)
    
    # Think about this brain teaser on your own!
    x = 12
    b = 3
    result2 = subtract(b, x)
    print("second result of subtract:", result2)

main()    


# Side note (you'll see this in the p6_utils.py file)
# if __name__ == "__main__":
# this makes it so that the main code doesn't
# run if this file is imported as a module
# future

# runfile('/Users/felix/Dropbox/ds2001/p6_functions/p6.py', wdir='/Users/felix/Dropbox/ds2001/p6_functions')
