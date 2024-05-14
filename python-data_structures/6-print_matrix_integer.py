#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length, i = len(matrix), 0

    while i < length:
        print("{}" .format(matrix[i]))
        i += 1


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()
