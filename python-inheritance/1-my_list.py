#!/usr/bin/python3
""" MyList Class
    Module that creates a class MyList that inherits from list
"""


class MyList(list):
    """"function that defines a class MyList


    """

    def print_sorted(self):
        """Public instance method that prints the list, in ascending order
        """
        print(sorted(self))
