#!/usr/bin/python3
"""Square and instance, size as private variable"""

class Square:
    """"This is a class, Square
        with a private instance attribute, size."""

    def __init__(self, size):
        """Initialization function that initializes
            a new instance attribute
            Args:
            size: instance attribute."""
        self.__size = size
