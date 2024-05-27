#!/usr/bin/python3
"""Defines a function that a serialzed string"""
import json


def to_json_string(my_obj):
    """function returns JSON representation of object
    Args:
        my_obj: object to serialize
    Return:
        serialized object
    """

    ret = json.dumps(my_obj)
    return ret
