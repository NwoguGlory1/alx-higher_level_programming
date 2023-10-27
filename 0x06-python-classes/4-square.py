#!/usr/bin/python3
"""Square with a private instance attribute of type, integer, less than 0.
    raises either a TypeError or a ValueError, if otherwise
    uses getter and setter to control the type and value."""


class Square:
    """This is a class, Square."""

    def __init__(self, size=0):
        """Initializes size to 0.


            Args:
            size: instance attribute.


            Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size

    @property
    def size(self):
        """Getter for private attribute, size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for private attribute, size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method that calculates the current square area"""
        return (self.__size * self.__size)
