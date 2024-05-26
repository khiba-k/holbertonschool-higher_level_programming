#!/usr/bin/python3
"""function that returns True if the object is an instance of, or if the object

   is an instance of a class that inherited from, the specified class;
   otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """checks if object is instance of a class that inherited from a_class

    Args:
        obj: object
        a_class: class

    Returns:
        True or False
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
