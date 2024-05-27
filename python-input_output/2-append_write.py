#!/usr/bin/python3
"""Defines function that appends to txt file"""


def append_write(filename="", text=""):
    """function appends text to file
    Args:
        filename: file to append to
        text: text to append
    Return:
        returns num of characters of text
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    num = len(text)
    return num
