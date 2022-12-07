#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        best = ''
        for i in a_dictionary.keys():
            if a_dictinary[i] > best:
                best = i
        return a_dictionary[best]
