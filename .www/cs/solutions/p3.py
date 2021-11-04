# Felix Muzny
# DS 2001 - Computer Science
# September 22/23, 2021
# Practicum 3 - reading files and conditionals

import matplotlib.pyplot as plt # so that we can graph things

def main():
    print("practicum 3")

    # Task 1
    neighborhood = input("What neighborhood? ")
    fname = neighborhood + ".txt"
    f = open(fname, "r")
    size = float(f.readline())
    pop = int(f.readline())
    age = int(f.readline())
    f.close()

    print("Information about", neighborhood)
    print("Size:", size)
    print("Population:", pop)
    print("Median age:", age)
    print()
    #Group Question answer

    # Task 2 - ideal neighborhood
    ideal_size = float(input("Ideal size?"))
    ideal_pop = int(input("Ideal population?"))
    ideal_age = int(input("Ideal age?"))
    print()

    # solution using abs()
    match_count = 0 # Students will likely struggle here    
    if abs(size - ideal_size) <= 0.25:
        print(neighborhood, "fits your size criteria.")
        match_count += 1
    else:
        print(neighborhood, "does not fit your size criteria.")

    # example not using abs()
    if ideal_pop - pop <= 3000 and ideal_pop - pop >= -3000:
        print(neighborhood, "fits your population criteria.")
        match_count += 1
    else:
        print(neighborhood, "does not fit your population criteria.")

    if abs(ideal_age - age) <= 4:
        print(neighborhood, "fits your age criteria.")
        match_count += 1
    else:
        print(neighborhood, "does not fit your age criteria.")

    if match_count == 3:
        print("Congrats! It's a match!")
    elif match_count > 0:
        print("It's a so-so match.")
    else:
        print("It's not a match. :(")

        # Task 3 - load a new neighborhood

        compare_n = input("Compare against? ")
        fname = compare_n + ".txt"
        with open(fname, "r") as f:
            c_size = float(f.readline())
            c_pop = int(f.readline())
            c_age = int(f.readline())

        if c_size > size:
            print(compare_n + "'s size is higher")
        else:
            print(compare_n + "'s size is lower")

        if c_pop > pop:
            print(compare_n + "'s population is higher")
        else:
            print(compare_n + "'s population is lower")

        if c_age > age:
            print(compare_n + "'s age is higher")
        else:
            print(compare_n + "'s age is lower")

        # Task 4 - graph the data
        plt.plot("size", size, "s", label = neighborhood)
        plt.plot("size", c_size, "s", label = compare_n)
        plt.legend()
        plt.title("Statistics for " + neighborhood +" vs. " + compare_n)
        plt.show()
        plt.plot("population", pop, "s", label = neighborhood)
        plt.plot("population", c_pop, "s", label = compare_n)
        plt.plot("age", age, "s", label = neighborhood)
        plt.plot("age", c_age, "s", label = compare_n)
        plt.legend()
        plt.title("Statistics for " + neighborhood +" vs. " + compare_n)
        plt.show()

main()
