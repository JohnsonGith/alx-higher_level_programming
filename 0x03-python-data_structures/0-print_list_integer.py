#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Write a function that prints all integers of a list."""
    for n in range(len(my_list)):
        print("{:d}".format(my_list[n]))
