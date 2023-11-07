#!/usr/bin/python3
"""
Function that returns True if the object is exactly an instance
of specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
