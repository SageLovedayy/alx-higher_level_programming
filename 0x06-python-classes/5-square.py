#!/usr/bin/python
"""printing a square"""


class Square:
    """defines a square class"""
    def __init__(self, size=0):
        """initializes class"""
        self.size = size

    @property
    def size(self):
        """getter of size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns area of square"""
        return (self__size * self__size)

    def my_print(self):
        """prints square with character # in stdout"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
