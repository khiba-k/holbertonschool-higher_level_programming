#!/usr/bin/python3
def print_square(size):
    width, height 0, 0

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

