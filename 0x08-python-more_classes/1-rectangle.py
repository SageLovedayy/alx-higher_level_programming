#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """defines rec with width and height"""
    def __init__(self, width=0, height=0):
        """Initializes rectangle instances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter to retrieve width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter to set width"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
