#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []

    new.extend(my_list)
    index = new.index(search)
    new[index] = replace

    return new
