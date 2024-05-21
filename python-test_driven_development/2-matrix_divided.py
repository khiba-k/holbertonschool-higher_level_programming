#!/usr/bin/python3
"""
    Function divides all elements of a matrix

    Example:
        matrix = [
        [1, 2, 3],
        [4, 5, 6]
        ]
        print(matrix_divided(matrix, 3))
        print(matrix)

        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        [[1, 2, 3], [4, 5, 6]]

"""

def matrix_divided(matrix, div):
    """
        Args:
            matrix: The matrix list.
            div: value to divide matrix elements by.

        Returns:
            New matrix with divided elements.
    """

    lst = []

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    for row in matrix:
        new_row = []
        for element in row:
            c = round(element / div, 2)
            new_row.append(c)
        lst.append(new_row)

    return lst
