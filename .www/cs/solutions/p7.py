"""
Felix Muzny
October 20/21, 2021
DS 2001 - CS Practicum #7

A program to analyze a csv of boston crime data as a 
list of lists and analyze day-of-the-week trends.
"""


import p7_utils
import matplotlib.pyplot as plt

FILENAME = "boston-incident-reports-march2020-tiny.csv"
DAY_OF_WEEK = 4
OFFENSE_DESC = 1
INVESTIGATE = "AUTO THEFT"


def get_column(data, index):
    """
    name: get_column
    This function takes a list of lists and an integer and gives the user the list of values from the indicated column. Does not change the passed in list of lists.
    data - list of lists
    index - integer indicating which column values to access
    return:
    List of values where the first value is the value at position "index" from the first row in data, the second value is the value at position "index" from the second row in data, etc for all rows in data
    """
    column = []
    for row in data:
        column.append(row[index])
    return column

def exact_match(data, index, target_value):
    """
    name: extact_match
    This function takes a list of lists of values and returns a new list of lists containing only rows from the original data where the value at column index matches the provided target value.
    parameters:
    data - list of names
    index - column to look in
    target_value - value to match
    return:
    a new list of lists containing all target rows
    """
    filtered = []
    for row in data:
        if row[index] == target_value:
            filtered.append(row)
    return filtered

def unique_values(lst):
    """
    name: unique_values
    This function takes a list of values and returns a list containing only one copy of every value in the given list, in sorted order.
    parameters:
    lst - list of values
    return:
    a new list of unique values, in sorted order
    """
    unique = []
    for value in lst:
        if value not in unique:
            unique.append(value)
    unique.sort()  # mutator function
    return unique

def day_graph(data):
    """
    name: day_graph
    This function takes a list of lists and makes a graph of
    day counts in order from Monday -> Sunday.
    parameters:
    data - list of lists of data
    return:
    none
    """
    in_order_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    counts = []
    for d in in_order_days:
        # count up the incidents
        counts.append(len(exact_match(data, DAY_OF_WEEK, d)))
    print(in_order_days)
    print(counts)
    plt.bar(in_order_days, counts)
    plt.xlabel("Day of incident")
    plt.ylabel("Count")
    plt.show()


if __name__ == "__main__":
    print("p7")
    # reading in the data
    data = p7_utils.read_csv(FILENAME)

    print("Number of rows:", len(data))
    print(data[:3])


    # Task 2
    days = get_column(data, DAY_OF_WEEK)
    print("length of column list (should be", len(data), "):", len(days))

    # Task 3
    plt.hist(days)
    plt.xlabel("Day of Incident")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.show()


    # Task 4
    # in order graph of incidents
    # you'll need to hardcode in the order
    # because alphabetic/other orders don't make sense for us
    day_graph(data)

    # Task 5 getting the unique values
    # Sanity check by looking at the days
    print("days:", unique_values(days))
    offenses = get_column(data, OFFENSE_DESC)
    offense_types = unique_values(offenses)
    print("offense types:", offense_types)

    # Task 5 investigation
    offense_subset = exact_match(data, OFFENSE_DESC, INVESTIGATE)
    day_graph(offense_subset)

    # or, using the hist function
    offense_days = get_column(offense_subset, DAY_OF_WEEK)
    plt.hist(offense_days)
    plt.xlabel("Day of Incident")
    plt.ylabel("Count")
    plt.show()

    
