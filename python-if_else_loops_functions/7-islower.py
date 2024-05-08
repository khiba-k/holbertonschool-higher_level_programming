#!/usr/bin/python3
def islower(c):
    deci = ord(f"{c}")
    if deci > 96 and deci < 123:
        return 1
    else:
        return 0
