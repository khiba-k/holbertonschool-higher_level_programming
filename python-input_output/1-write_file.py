#!/usr/bin/python3
""" Defines function that writes to txt file"""


def write_file(filename="", text=""):
    """function writes text to file
    Args:
        filename: name of file to write to
        text: text to write
    Return:
        returns number of characters
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    num = len(text)
    return num
