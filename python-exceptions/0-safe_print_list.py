#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i, length = 0, 0
    container = ""

    for loop in my_list:
        length += 1
    try:
        if x <= length:
            while i < x:
                container += str(my_list[i])
                i += 1
            print("{}" .format(container))
        else:
            print(f"{my_list}")
        return length
    except IndexError:
            print(f"{my_list}")
            return length

    return x
