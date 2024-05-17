#!/usr/bin/python3
def best_score(a_dictionary):
    greatest = -1
    greatKey = None

    for key, value in a_dictionary.values():
        if value > greatest:
            greatest = value
            greatKey = key

    return greatkey
