#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """defines rec with width and height"""
    def __init___(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter to retrieve width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter to retrieve height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
