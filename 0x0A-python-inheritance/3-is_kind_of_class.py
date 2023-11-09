#!/usr/bin/python3
"""check if it is instance of class and inheritance"""


def is_kind_of_class(obj, a_class):
    """ Write a function that returns True
    if object is an instance of, or if object
    is an instance of a class that inherited from
    Args:

    obj: the object to check
    a_class: the class to check from

    Returns: True if or False else
"""
    return (isinstance(obj, a_class))
