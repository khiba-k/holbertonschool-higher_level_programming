#!/usr/bin/python3

"""
    Function divides all elements of a matrix

    Example:
       a = 5
       b = 10

       add_integer(a, b)

       15
"""

def add_integer(a, b=98):
    """
        Args:
            a: first integer
            b: second integer

        Returns:
            Sum of the two integers
    """
    result = 0

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    elif a is type(float):
        a = int(a)
    elif b is type(float):
        b = int(b)
    result = a + b

    return int(result)
