#!/usr/bin/python3
def islower(c):
    deci = ord(c)
    if deci <= 97 or deci < 123:
        print(f"{c} is lower")
    else:
        print(f"{c} is upper")
