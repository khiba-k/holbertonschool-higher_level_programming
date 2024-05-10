#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    res = 0

    for x in argv:
        if x == argv[0]:
            print("{}" .format(0))
        else:
            i = int(x)
            res += i
            if x == argv[-1]:
                print("{}" .format(res))
