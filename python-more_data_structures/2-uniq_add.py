#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    my_set = set(my_list)

    for x in my_set:
        res += x

    return res
