#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    new.extend(my_list)
    
    replaced = False
    
    for i in range(len(new)):
        if new[i] == search:
            new[i] = replace
            replaced = True

    if not replaced:
        return my_list
