#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for i in a_dictionary.keys():
        if a_dictionary[i] == value:
            del new_dict[i]
    return new_dict
