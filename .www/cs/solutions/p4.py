"""
Felix Muzny
September 29/30th, 2021
DS 2001 - CS Practicum #4

A program to read and analyze enrollment information
over a span of 2010 - 2020.
"""
import random
import matplotlib.pyplot as plt

def main():
    print("practicum 4!")

    # Task 1 read the file into a list
    enrollments = []
    filename = "enrollment.txt"
    infile = open(filename, "r")
    while True:
        line = infile.readline()
        if line == "":
            break
        # cast to an int where we know it won't be ""
        enrollments.append(int(line))
    infile.close()
    print("finished reading in the file!")

    print()

    print("number of data points:", len(enrollments))
    print("Enrollments:", enrollments)


    # Re-ordered so that both files are read in first
    # then we'll only need to do the graphing once
    # note that this code is **very** similar to the 
    # reading enrollments code. Remember this for later!
    # we want to make it so that we don't need to do this
    # copy + pasting!
    #
    # Task 3 read the file into a list
    ftfy_enrollments = []
    filename = "firsttime_firstyear.txt"
    infile = open(filename, "r")
    while True:
        line = infile.readline()
        if line == "":
            break
        ftfy_enrollments.append(int(line))
    infile.close()
    print("finished reading in the file!")

    print()

    print("number of data points:", len(ftfy_enrollments))
    print("First Time First Year Enrollments:", ftfy_enrollments)

    # Task 2: graph data points from our list
    year = 2010
    i = 0
    while i < len(enrollments):
        plt.plot(year, enrollments[i], ".")
        plt.plot(year, ftfy_enrollments[i], "s")
        year += 1
        i += 1
    # plt.show() is used to display the graph if we want to 
    # make multiple graphs with the data points on different graphs
    plt.show()
    print()

    # Example with a for loop instead
    for i in range(len(enrollments)):
        year = i + 2010
        plt.plot(year, enrollments[i], ".")
        plt.plot(year, ftfy_enrollments[i], "s")
    plt.show() 
    
    # Task 4
    user_year = int(input("Year? "))
    year_index = user_year - 2010
    enrollment = enrollments[year_index]
    ftfy_enrollment = ftfy_enrollments[year_index]

    odds = round((ftfy_enrollment / enrollment) * 100)
    print("Enrollment:", enrollment)
    print("First Time First Year Enrollment:", ftfy_enrollment)
    print("Odds:", str(odds) + "%")
    
    student = random.randint(1, enrollment)
    print("I've chosen a student!")
    guess = input("Do you think that the student I've selected is a first time first year student (y/n)? ")

    is_ftfy = student <= ftfy_enrollment
    if (guess == "y" and is_ftfy) or (guess == "n" and not is_ftfy):
        print("Congratulations, you won!")
    else:
        print("Too bad! The student was not a first time first year student.")
    
    print("I chose student number:", student)

main()
