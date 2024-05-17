#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    alpha = sorted(a_dictionary.keys())

    for x in alpha:
        print(f"{x}: {a_dictionary[x]}")

