#!/usr/bin/python3
# -*- coding: UTF-8 -*-
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

         @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size
