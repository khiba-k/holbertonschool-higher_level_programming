#!/usr/bin/python3
"""defines class student"""


class Student:
    """class has attributes of students"""

    def __init__(self, first_name, last_name, age):
        """Method initializes student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method retrieves dictionary representation of student"""
        return self.__dict__
