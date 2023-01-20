#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = float(a / b)
    except ZeroDivisionError:
        x = None
        pass
    finally:
        print("Inside Result: {}".format(x))
        return x
