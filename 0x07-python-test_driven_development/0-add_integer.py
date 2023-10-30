#!/usr/bin/python3
def add_integer(a, b=98):


    """
Function that adds two integers.


Returns an integer:
    the addition of a and b.
    If b is not provided, it defaults to 98.


Args:
    a (int): An integer or float value.
    b (int): An integer or float value (default is 98).


Raises:
    Type Error exception if the argument type is otherwise.
    The error message:
    sa must be an integer or b must be an integer.
"""


    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")


    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a) + int(b)
