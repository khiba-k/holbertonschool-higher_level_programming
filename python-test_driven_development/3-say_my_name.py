#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == None:
        raise ValueError("missing first name")
    if last_name == None:
        raise ValueError("missing last name")

    print("My name is {} {}" .format(first_name, last_name))
