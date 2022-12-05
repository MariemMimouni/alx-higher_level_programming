#!/usr/bin/python3
def no_c(my_string):
    L = list(my_string)
    for i in L:
        if i in ['c', 'C']:
            L.remove(i)
    return(''.join(L))
