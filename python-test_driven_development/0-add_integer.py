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
    elif a is None or b is None:
        raise ValueError("missing one argument")
    elif a is None and b is None:
        raise ValueError("missing both arguments")
    elif a is type(float):
        a = int(a)
    elif b is type(float):
        b = int(b)
    result = a + b

    #if math.isinf(result):
       # raise OverflowError("result is too large")
    print(f"res {result}")
    return result

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
