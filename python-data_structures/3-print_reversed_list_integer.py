#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = []
    rev.append(my_list.reverse())
    for x in rev:

        print("{:d}" .format(x))
