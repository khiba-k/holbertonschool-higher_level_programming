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

    chars_to_check = ['.', '?', ':']
    result = []
    i = 0

    while i < len(text):
        if text[i] in chars_to_check:
            result.append(text[i])
            result.append("\n\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            result.append(text[i])
            i += 1
    print("".join(result))
