#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            string += x

    print("{}" .format(string))
