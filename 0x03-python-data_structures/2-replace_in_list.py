#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """write function that replace elment of a list."""
    element = 8
    if idx < 0 or idx > (range(my_list) - 1):
        return my_list

    my_list[idx] = element
    return my_list
