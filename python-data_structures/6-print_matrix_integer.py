#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length, i, = len(matrix), 0
 
    if not matrix[0]:
        print()
    while i < length:
        row, j = matrix[i], 0

        while j < len(row):
            if j == len(row) - 1:
                print("{:d}" .format(row[j]))
            else:
                print("{:d}" .format(row[j]), end=" ")
            j += 1
        i += 1
