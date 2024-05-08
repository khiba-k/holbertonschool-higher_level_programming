#!/usr/bin/python3
def islower(c):
    if isinstance(c, int):
        traceback.print_exc()
    deci = ord(f"{c}")
    if deci > 96 and deci < 123:
        return 1
    else:
        return 0
