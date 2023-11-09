#!/usr/bin/python3
"""writing a base geometry class"""


class BaseGeometry:
    """ BaseGeometry class with a public instance method """
    def area(self):
        """This raises an exception for area not def"""
        raise Exception("area() is not implemented")
