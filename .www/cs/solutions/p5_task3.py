#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felix Muzny
October 6/7, 2021
DS 2001 - CS Practicum #5

A program to read comments and perform sentiment analysis, through Task 3
"""
import matplotlib.pyplot as plt


def main():
    print("practicum 5! Sentiment analysis")
    
    # Task 1 - all group questions!
    
    # Task 2
    positive = []
    infile = open("positive_words.txt", "r")
    while True:
        line = infile.readline()
        if line == "":
            break
        # leave lines as strings, but use .strip() to remove the \n
        positive.append(line.strip())
    infile.close()
    print("Number of positives:", len(positive))
    print(positive[:3]) 
    
    
    # an example with using a for loop!
    negative = []
    infile = open("negative_words.txt", "r")
    for line in infile:
        # leave lines as strings, but use .strip() to remove the \n
        negative.append(line.strip())
    infile.close()
    print("Number of negatives:", len(negative))
    print(negative[:3])    
    
    comments = []
    infile = open("comments.txt", "r")
    while True:
        line = infile.readline()
        if line == "":
            break
        # leave lines as strings, but use .strip() to remove the \n
        comments.append(line.strip().lower())
    infile.close()
    print("Number of comments:", len(comments))
    print(comments[:3])
    print()
    
    
    # Task 3 sentiment for one comment
    comment = comments[0] # grab the first comment
    print(comment)
    comment = comment.split()
    score = 0
    for i in range(len(comment)):
        if comment[i] in positive:
            score += 1
            print("pos word:", comment[i])
        elif comment[i] in negative:
            score -= 1
            print("neg word:", comment[i])
    print("score:", score)
        
main()
