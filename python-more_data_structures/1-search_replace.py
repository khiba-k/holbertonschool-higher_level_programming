#!/usr/bin/python3
def search_replace(my_list, search, replace):

    my_index = lambda search: mylist.index(search)
    my_list[my_index] = replace
    return my_list

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
