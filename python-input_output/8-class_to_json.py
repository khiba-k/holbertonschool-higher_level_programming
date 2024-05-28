#!/usr/bin/python3
"""Defines function that returns dictionary"""


def class_to_json(obj):
    """Function returns dictionary

    Args:
        obj: instance of class
    Return:
        Returns a dictionary
    """
    return obj.__dict__
