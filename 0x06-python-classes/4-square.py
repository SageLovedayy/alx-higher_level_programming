#!/usr/bin/python3
"""Create square class"""


class Square:
    """square class - defines square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter -square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter -square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area"""
        return (self.__size * self.__size)
