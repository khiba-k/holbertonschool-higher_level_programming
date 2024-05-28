#!/usr/bin/python3
"""Adds all arguments to python list"""
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file


ret = load_from_json_file("add_item.json")
lst = []
lst.extend(sys.argv[1:])
save_to_json_file(lst, "add_item.json")
