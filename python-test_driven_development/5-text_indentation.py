#!/usr/bin/python3
def text_indentation(text):
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
