#!/usr/bin/python3
"""
Function that returns True if the object is exactly an instance
of specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        a = 1

        return True
    else:
        return False
