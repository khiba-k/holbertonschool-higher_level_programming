#!/usr/bin/python3
"""Defines class and serializes it"""
import pickle


class CustomObject:
    """class displays attributes
    Args:
        name: string
        age: integer
        is_student: boolean
    """
    def __init__(self, name, age, is_student):
        """method initializes object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method prints out attributes"""
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """method serializes the current instance of the object"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        """method returns instance of custom object"""
        try:
            with open(filename, "rb") as f:
                ret = pickle.load(f)
            return ret
        except:
            return None
