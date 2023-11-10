#!/usr/bin/python3
"""writing a base geometry class"""


class BaseGeometry:
    """ BaseGeometry class with a public instance method """
    def area(self):
        """This raises an exception for area not def"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
