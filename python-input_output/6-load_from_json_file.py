#!/usr/bin/python3
"""Defines function that loads object from JSON file"""
import json


def load_from_json_file(filename):
    """function creates object from JSON
    Args:
        filename: name of file to to load from
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
