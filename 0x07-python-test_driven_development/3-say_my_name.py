#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    This is a module that prints My name is <first name> <last name>

    Args:
    first_name: must be a string
    last_name: must be a string

    Return:
    My name is <first name> <last name>

    Raises:
    TypeError: first_name must be a string or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
