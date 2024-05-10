#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)

    if l != 2:
        print("{} arguments:" .format(l - 1))
    elif l == 1:
        print("{} arguments." .format(l - 1))
    else:
        print("{} argument:" .format(l - 1))

    for i, x in enumerate(argv):
        if x == argv[0]:
            continue
        print("{}: {}" .format(i,x))
