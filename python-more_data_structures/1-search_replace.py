#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    new.extend(my_list)

    if search not in new:
        return new
    else:
        index = new.index(search)
        new[index] = replace

    return new
