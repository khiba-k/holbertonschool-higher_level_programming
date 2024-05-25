#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """
    Class Rectangle defines a Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle with width and height
    

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets width of rectangle

        Returns:
             width of rectangle
        """
        return self.width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @height
    def height(self):
        """
        Gets value of rectangle

        Returns:
            Height of rectangle
        """
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
