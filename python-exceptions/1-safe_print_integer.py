#!/usr/bin/python3
def safe_print_integer(value):

    try:
        val = int(value)
        print("{:d}" .format(value))
        return True
    except (TypeError, ValueError):
        return False
