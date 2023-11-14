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
    def to_json_string(list_dictionaries):
        """Static method that returns JSON rep of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes JSON string rep of list_objs to a file"""
        jlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                jlist.append(i.to_dictionary())

        op = cls.to_json_string(jlist)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(op)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)


    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"


        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
                json_list = json.loads(json_string)
                return [cls.create(**obj) for obj in json_list]
        except FileNotFoundError:
            return []


    @classmethod
    def create(cls, **kwargs):
        """Creates and returns an instance of the class with given attributes."""
        instance = cls(1, 1)  # You may need to adjust the default values
        instance.update(**kwargs)
        return instance

