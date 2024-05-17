#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return None
    valid_items = {k: v for k, v in a_dictionary.items() if v is not None}
    if not valid_items:
        return None
    best_key = max(valid_items, key=valid_items.get)
    return best_key
