#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i, j in a_dictionary.items():
        a_dictionary[i] = 2 * j
    return a_dictionary
