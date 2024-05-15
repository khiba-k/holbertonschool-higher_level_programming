#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        newR = []
        for col in row:
            newR.append(pow(col, 2))
        new.append(newR)
    return new
