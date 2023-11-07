#!/usr/bin/python3
"""
Function that returns True if the object is exactly an instance
of specified class; otherwise False.
"""


def is_same_class(obj, a_class):

    if isinstance(obj, a_class):
        return True
    else:
        return False
