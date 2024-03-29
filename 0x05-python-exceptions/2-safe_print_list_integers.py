#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if x == 0:
        print()
        return 0
    try:
        p = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                p += 1
            except TypeError:
                pass
            except ValueError:
                pass
    except IndexError:
        pass
    print()
    return p
