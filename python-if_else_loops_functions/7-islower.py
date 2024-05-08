#!/usr/bin/python3
def islower(c):
    if isinstance(c, int):
        traceback.print_exc()
    deci = ord(f"{c}")
    if deci > 96 and deci < 123:
        print(f"{c} is lower")
        return 1
    else:
        print(f"{c} is upper")
        return 0

islower(3)
