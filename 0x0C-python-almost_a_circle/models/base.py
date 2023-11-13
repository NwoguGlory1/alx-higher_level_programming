#!/usr/bin/python3
"""Function with class, Base made for managing id attribute"""
import json

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

    @staticmethod
    def to_json_string(list_objs):
        """Static method that returns JSON rep of list_objs"""
        if list_objs is None or len(list_objs) == 0:
            return "[]"
        else:
            return json.dumps([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes JSON sting rep of list_objs to a file"""
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([list_objs])

        with open(filename, "w") as file:
                file.write(json_string)
