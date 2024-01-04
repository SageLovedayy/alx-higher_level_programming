#!/usr/bin/python3
"""
Module: rectangle

Defines the Rectangle class with private attributes width and height.
Provides methods to calculate area and perimeter, allows printing
using any given symbol,
deletes instances, keeps track of the number of instances, and has
a static method that
returns the bigger rectangle out of two given rectangles.
"""


class Rectangle():
    """
    Rectangle class represents a geometric rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): Number of instances created and not deleted.
        print_symbol (any type): Used to print string representation.

    Methods:
        __init__(self, width=0, height=0): Initializes new Rectangle instance.
        __del__(self): Deletes the instance of the rectangle and decrements
        the count of instances.
        width(self): Getter method for retrieving the width of the rectangle.
        width(self, value): Setter method for setting width of the rectangle.
        height(self): Getter method for retrieving the height of the rectangle.
        height(self, value): Setter method for setting height of the rectangle.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle with
        the specified print symbol.
        __repr__(self): Returns a string representation to recreate
        a new instance of the rectangle.
        @staticmethod
        bigger_or_equal(rect_1, rect_2): Static method that returns the bigger
        rectangle out of two given rectangles.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """
        Deletes the instance of the rectangle and decrements the count
        of instances.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Args:
            value (int): The width to be set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): The height to be set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
            If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle with
        the specified print symbol.

        Returns:
            str: A string representing the rectangle with
            the specified print symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """
        Returns a string representation to recreate a new
        instance of the rectangle.

        Returns:
            str: A string representation to recreate a new
            instance of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the bigger rectangle out
        of two given rectangles.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The bigger or equal rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
