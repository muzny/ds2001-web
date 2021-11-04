#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felix Muzny
October 6/7th, 2021 -> re-write for the 13/14th
DS 2001 - CS Practicum #5 -> Practicum #6

A program to read comments and perform sentiment analysis
"""
import matplotlib.pyplot as plt


# functions:
# three parts: name, parameters, return
# name - file_to_list
# params - filename (str)
# return - list of strings

# why do I want to write a function?
# helps "modularize" the code
# re-use code w/o copy-pasting! :)


def file_to_list(filename):
    # filename = the first (only) value passed in
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
    infile = open(filename, "r")
    for line in infile:
        # leave lines as strings, but use .strip() to remove the \n
        ls.append(line.strip())
    infile.close()
    return ls

# Task 3 is a great candidate for a function as well!
def score_comment(comment, positive, negative):
    """
    name: score_comment
    
    evaluates the sentiment of one text string based on word
    lists of positive and negative words.

    Parameters
    ----------
    comment : string
        the comment to score.
    positive: list of strings
        positive word list, assumed to be all lower case
    negative: list of strings
        negative word list, assumed to be all lower case

    Returns
    -------
    score : int
        the sentiment value of the passed in comment.

    """
    comment = comment.split()
    score = 0
    for i in range(len(comment)):
        # added call to .lower() here because the list of 
        # comments is no longer lowercase! 
        # lots of ways to deal with this though. :)
        if comment[i].lower() in positive:
            score += 1
            # debugging prints
            #print("pos word:", comment[i])
        elif comment[i].lower() in negative:
            score -= 1
            # debugging prints
            #print("neg word:", comment[i])
    return score

def main():
    print("practicum 5! Sentiment analysis")
    print()
    
    # Task 1 - all group questions!
    
    # Task 2
    positive = file_to_list("positive_words.txt")
    print("Number of positives:", len(positive))
    print(positive[:3]) 
    print()
    
    # an example of reading a file using a for loop!
    negative = file_to_list("negative_words.txt")
    print("Number of negatives:", len(negative))
    print(negative[:3])    
    print()
    
    comments = file_to_list("comments.txt")
    print("Number of comments:", len(comments))
    print(comments[:3])
    print()
    
    # Task 5 - get the scores and then 
    # graph them
    print("Scoring the comments:")
    scores = []
    # Task 4 go over all of the comments
    for comment in comments:
        # Task 3 sentiment for one comment
        # but using a function to do so!
        print(comment)
        score = score_comment(comment, positive, negative)
        print("score:", score)
        print()
        scores.append(score)
        
    # Task 5 - first graph!
    y_vals = [0 for score in scores]
    plt.plot(scores, y_vals, ".")
    plt.xlabel("sentiment score")
    plt.title("sentiment scores")
    plt.show()
    
    # Task 5 - second graph!
    # now, as a histogram!
    plt.hist(scores)
    plt.xlabel("sentiment score")
    plt.ylabel("count")
    plt.title("count of sentiment scores for vaccination comments")
    plt.show()

main()
