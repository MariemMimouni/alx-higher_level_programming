#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(i)):
            print(matrix[i][j], end="")
            if j != len(i) - 1:
                print(' ', end="")
        if i != len(matrix) - 1:
            print()
