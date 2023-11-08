#!/usr/bin/python3
"""
A class that defines Student with its attributes;
constructor, methods
"""


class Student:
    """ An object serializer
    """

    def __init__(self, first_name, last_name, age):
        """
        instantiation with first_name,last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This returns the dictionary description
        of a Student instance, attrs
        """
        if isinstance(attrs, list) and
            all(isinstance(x, str) for x in attrs)):
                return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
            return self.__dict__
