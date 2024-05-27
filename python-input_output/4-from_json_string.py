#!/usr/bin/python3
"""Defines function that returns data structure"""
import json


def from_json_string(my_str):
    """Function returns object from JSON string
    Args:
        my_str: JSON string
    Return:
        Returns python object
    """

    ret = json.loads(my_str)
    return ret
