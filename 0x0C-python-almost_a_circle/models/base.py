#!/usr/bin/python3
"""Function with class, Base made for managing id attribute"""


class Base:
    """ Created the class, Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
