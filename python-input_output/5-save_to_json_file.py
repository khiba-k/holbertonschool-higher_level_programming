#!/usr/bin/python3
"""
5-save_to_json_file.py writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): python object
        filename (str): name of the file to write to
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
