#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i, length = 0, 0

    for x in my_list:
        length += 1
    try:
        if x <= length:
            while i < x:
                if i == x - 1:
                    print({} .format(mylist[i])
                else:
                    print({} .format(mylist[i], end="")
    except:
        print("X is larger than the length of the list")

    return x
