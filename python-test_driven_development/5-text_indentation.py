#!/usr/bin/python3
"""
    Function divides all elements of a matrix

    Example:
       first_name = "Khiba"
       last_name = "Koenane"

       say_my_name(first_name, last_name)

       Khiba Koenane
"""


def text_indentation(text):

    """
        Args:
            first_name: first name
            last_name: second name

        Returns:
            A sentence with the first and last name
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
