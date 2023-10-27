#!/usr/bin/python3
"""Square with a private instance attribute of type, integer and less than 0.
    raises either a TypeError or a ValueError, if otherwise."""


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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
