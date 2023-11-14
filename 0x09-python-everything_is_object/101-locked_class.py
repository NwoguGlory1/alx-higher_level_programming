#!/usr/bin/python3
"""Locking a class against props"""


class LockedClass:
    """creating a locked class that
    prevens creaion of another instance attribute except if 
    the new instance is called first_name.
    """

    __slots__ = ["first_name"]
