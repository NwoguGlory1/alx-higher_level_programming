#!/usr/bin/python3

"""
* lookup - returns the list of available attributes
* and methods of an object
* @obj: object
* Returns: list object
*/
"""


def lookup(obj):
    """
    returns available attributes
    and methods in an object.
    """
    return (dir(obj))
