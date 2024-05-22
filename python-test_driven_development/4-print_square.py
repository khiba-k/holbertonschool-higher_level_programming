#!/usr/bin/python3

"""
    Function divides all elements of a matrix

    Example:
       size = 2

       print_square(size)

       ##
       ##
"""

def print_square(size):
    """
        Args:
            size: size of square

        Returns:
            a square the size of square arg
    """
    width, height = 0, 0

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    while height < size:
        while width < size:
            print("#", end="")
            width += 1
        print()
        height += 1

