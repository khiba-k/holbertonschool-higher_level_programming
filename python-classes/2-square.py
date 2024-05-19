#!/usr/bin/python3

"""
1-square.py: is a class Square that defines a square
"""


class Square:
    """class Square that defines a square

        Attributes:
        attr1 (size): Size of the Square.

    """

    def __init__(self, size=0):
        """Initializer with default size = 0"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

