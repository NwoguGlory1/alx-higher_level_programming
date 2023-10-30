#!/usr/bin/python3
def print_square(size):
    """
    This is a module that  prints a square with the character #

    Args:
    size: the size length of the square

    Return:
    a square with the character #

    Raises:
    TypeError: size must be an integer
    ValuError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
