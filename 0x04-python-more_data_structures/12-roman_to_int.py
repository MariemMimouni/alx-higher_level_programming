#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    else:
        Rs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        L = list()
        for i in roman_string:
            L.append(Rs[i])
        n = L[0]
        for j in range(1, len(L)):
            if L[j] > L[j-1]:
                n -= L[j-1]
                n += L[j] - L[j-1]
            else:
                n += L[j]
        return n
