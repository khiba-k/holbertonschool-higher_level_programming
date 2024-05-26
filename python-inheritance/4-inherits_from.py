#!/usr/bin/python3
"""function that returns True if the object is an instance of a class


   that inherited (directly or indirectly) from the specified class;
   otherwise False.
"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited
       from a class directly or indirectly

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
