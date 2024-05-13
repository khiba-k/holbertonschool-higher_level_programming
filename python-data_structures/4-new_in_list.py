#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    num = len(my_list) - 1
    if idx < 0 or idx > num:
        return my_list
    else:
        new = my_list.copy()
        new[idx] = element
        return new
