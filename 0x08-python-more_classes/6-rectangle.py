#!/usr/bin/python3
"""
A module for the class, Rectangle.
"""


class Rectangle:
    """
    An class, Rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializer"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieved width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ""
        for x in range(self.__height):
            for y in range(self.__width):
                rect += "#"
            if x != self.__height - 1:
                rect = rect + "\n"
        return rect

    def __repr__(self):
        """
        Returns the string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints rectangle with delete message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
