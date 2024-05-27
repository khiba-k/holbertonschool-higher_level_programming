#!/usr/bin/python3
"""function object to file as JSON"""
import json
import os


def save_to_json_file(my_obj, filename):
    """function writes object to text file
    Args:
        my_obj: object to write
        filename: file to write to
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

    os.chmod(filename, 0o644)
