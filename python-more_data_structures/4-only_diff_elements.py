#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    set_3 = set_1.difference(set_2)
    set_4 = set_2.difference(set_1)
    
    my_list = list(set_3.union(set_2))
    return set_3.update(set_4)
