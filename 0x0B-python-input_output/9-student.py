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

    def to_json(self):
        """
        This returns the dictionary description
        of a Student instance
        """
        return (self.__dict__)
