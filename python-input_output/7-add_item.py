#!/usr/bin/python3
"""Adds all arguments to python list"""
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


ret = load_from_json_file("add_item.json")
lst = []
lst.extend(sys.argv[1:])
save_to_json_file(lst, "add_item.json")
