#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_1, new_2 = [], []

    for x in set_1:
        if x not in  set_2:
            new_1.append(x)
    for y in set_2:
        if y not in set_1:
            new_2.append(y)

    return new_2.extend(new_1)
