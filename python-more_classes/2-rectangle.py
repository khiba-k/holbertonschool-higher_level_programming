#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """Defines rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets width of rectangle
            Returns:
                ValueError: if width is less than 0
                TypeError: if width not integer
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets/sets height of rectanglheightReturns:
                ValueError: if height is less than 0
                TypeError: if height not integer
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
