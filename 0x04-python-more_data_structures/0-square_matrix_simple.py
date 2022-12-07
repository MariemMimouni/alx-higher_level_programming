#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix2[i][j] = matrix[i][j] ** 2
    return matrix2
