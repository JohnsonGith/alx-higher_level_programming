#!/usr/bin/python3
def no_c(my_string):
    """function that removes all characters c and C from a string."""
    new_stirng = ""
    for n in range(len(my_string)):
        if my_string[n] != 'c' and my_string[n] != 'C':
            new_string += my_string[n]
            return new_string
