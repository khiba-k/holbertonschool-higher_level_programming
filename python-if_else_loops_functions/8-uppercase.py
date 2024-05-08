#!/usr/bin/python3
def uppercase(str):
    string = ""
    for x in str:
        if isinstance(x, int):
            string += x
        length = len(str)

        deci = ord(x)
        if deci > 96 and deci < 123:
            upper = deci - 32
            char = chr(upper)
            string += char

        else:
            char = chr(deci)
            string += char

    print("{}" .format(string))
