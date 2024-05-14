#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length, i, = len(matrix), 0
    
    if not matrix:
        print("1")
    while i < length:
        row, j = matrix[i], 0
        l = len(row)

        while j < l:
            if j == l - 1:
                print("{:d}" .format(row[j]))
            else:
                print("{:d}" .format(row[j]), end=" ")
            j += 1
        i += 1
