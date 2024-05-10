#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 1:
        print("{} arguments." .format(len(argv) - 1))
    elif len(argv) != 2:
        print("{} arguments:" .format(len(argv) - 1))
    else:
        print("{} argument:" .format(len(argv) - 1))

    for i, x in enumerate(argv):
        if x == argv[0]:
            continue
        print("{}: {}" .format(i, x))
