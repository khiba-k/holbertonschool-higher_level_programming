#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}

    for x in a_dictionary:
        double = a_dictionary[x] * 2

        new.update({x: double})

    return new
