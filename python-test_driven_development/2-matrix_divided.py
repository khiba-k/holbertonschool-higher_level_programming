#!/usr/bin/python3
def matrix_divided(matrix, div):
    lst = []

    # Check if the matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if each row has the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Perform the division
    for row in matrix:
        new_row = []
        for element in row:
            c = round(element / div, 2)
            new_row.append(c)
        lst.append(new_row)

    return lst
