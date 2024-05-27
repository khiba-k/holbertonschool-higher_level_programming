#!/usr/bin/python3
"""Defines a function that reads text file"""


def read_file(filename=""):
    """Function returns a UTF* text file
    Args:
        filename: name of file to read
    Return:
        UTF8 text file
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")
    return read_file
