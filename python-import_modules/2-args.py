#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv) - 1

    if l == 0:
        print("{} arguments.".format(l))
    elif l == 1:
        print("{} argument:".format(l))
    else:
        print("{} arguments:".format(l))

    if l >= 1:
        i = 0
        for x in argv:
            if i != 0:
                print("{}: {}".format(i, argv))
            i += 1
