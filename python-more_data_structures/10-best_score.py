#!/usr/bin/python3
def best_score(a_dictionary):
    ints = []

    for x in a_dictionary.values():
        ints.append(x)
        ints.sort()

    return ints[-1]
