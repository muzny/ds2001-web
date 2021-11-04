#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felix Muzny
October 27/28, 2021
DS 2001 - CS Practicum #8

Solutions to the the review problems from Practicum 8
"""


"""
PART 1 - OUTPUT AND LOOPS
"""

print("my fave num 1")
my_fave_num = 97
if my_fave_num > 0:
    print("so big")
if my_fave_num < 100:
    print("so small")
print()

print("my fave num 2")
my_fave_num = 13
if my_fave_num > 0:
    print("so big")
elif my_fave_num < 100:
    print("so small")
print()

print("birthday")
party = "birthday"
p = 0
while p < len(party):
    print(party[p] + party)
    p += 1
print()

print("doodads")
target = ""
doodads = ["bauble", "cat", "lamp", "stop sign"]
ind = 0
while ind < len(doodads):
    print(str(len(target)) + ": " + doodads[ind])
    target = doodads[ind]
    ind += 1
print()

print("skee ball")
s = "skee ball"
num = 0
while num < len(s):
    print(s[len(s) - num - 1])
    num += 1
print()

print("items")
amount = 1
items = ["toothbrush", "toothpaste", "volcano"]
i = 0
while i < len(items): 
    amount = amount + len(items[i])
    print(amount)
    i += 1
print()

"""
PART 1 - while loops # of executions
"""

"""
# this is an infinite loop
x = 10
y = 2
while y < x:
    print(x)
    x += 10
"""

print("animals")
x = 10
animals = ["cat", "dog", "bear"]
for animal in animals:
    print(x)
    x += 10
print()

print("ds 2001 1")
my_s = "ds2001"
index = 0
while index < len(my_s) - 2:
    index += 1
    print(my_s[index])
print()

print("ds 2001 2")
my_s = "ds2001"
for i in range(len(my_s)):
    print(my_s[i])
print()

"""
PART 1 - INNER LOOP EXECUTIONS
"""
print("inner loop 1")
# 3 * 4 = 12 inner loop executions
count = 0
while count < 3:
    count2 = 0
    while count2 < 4:
        print(count2)
        count2 += 1
    count += 1
print()

print("inner loop 2")
# 1 + 2 + 3 + 4 = 10 inner loop executions
for outer in range(5):
    count = 0
    print("outer:", outer)
    while count < outer:
        print("count:", count)
        count += 1
print()

print("two times with while")
target = "example"
two_times = ""
count = 0
while count < len(target):
    two_times = two_times + target[count] * 2
    count += 1
print(two_times)
print()

print("two times with for loop")
# with a for loop
target = "example"
two_times = ""
for letter in target:
    two_times = two_times + letter * 2
print(two_times)
print()

"""
PART 2 - WRITING FUNCTIONS
Note: these functions should all have function comments in an ideal world :)
"""
import random

def number_words(s):
    return len(s.split())

def sandwich(s1, s2):
    n = len(s1)
    new_s = s1 * n + s2 + s1 * n
    return new_s

def same_maximum(param1, param2):
    if type(param1) != type(param2):
        print("different types!")
    else:
        max1 = max(param1)
        max2 = max(param2)
        if max1 == max2:
            print("same max:", max1)
        else:
            print("different max!")

def sum_positives(ls):
    total = 0
    for num in ls:
        if num > 0:
            total += num
    return total

def course_number(course):
    return course[2:]

def roll_table(people):
    for person in people:
        s = person + ": "
        for i in range(5):
            s += str(random.randint(1, 6)) + " "
        print(s)

def roll_table_return(people):
    rolls = []
    for person in people:
        indiv_rolls = []
        for i in range(5):
            indiv_rolls.append(random.randint(1, 6))
        rolls.append(indiv_rolls)
    return rolls

# example function calls
if __name__ == "__main__":
    print("example function calls")
    print("number_words")
    print(number_words("hello there I'm glad that I'm studying"))
    print()

    print("sandwich")
    print(sandwich("a", "cheese"))
    print(sandwich("aba", "cheese"))
    print()

    print("same_maximum")
    same_maximum([1, 2], "b")
    same_maximum([1, 2], [-2, -5, 2])
    same_maximum([1, 2], [-2, -5, -3])
    print()
    
    print("sum_positives")
    print(sum_positives([1]))
    print(sum_positives([1, -7, 8, 6]))
    print(sum_positives([]))
    print()

    print("course_number")
    print(course_number("DS2000"))  
    print(course_number("CS4120"))  
    print()

    print("roll_table (print)")
    roll_table(["Felix", "Arushi"])
    roll_table(["Asa", "Smit", "Archit"])
    print()

    print("roll_table (return)")
    print(roll_table_return(["Felix", "Arushi"]))
    print(roll_table_return(["Asa", "Smit", "Archit"]))
    print()
