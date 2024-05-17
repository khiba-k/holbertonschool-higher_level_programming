#!/usr/bin/python3
def search_replace(my_list, search, replace):

    index = my_list.index(search)
    my_list[index] = replace

    return my_list
