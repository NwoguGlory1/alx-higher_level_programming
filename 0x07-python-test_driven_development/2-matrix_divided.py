#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    This is a module that divides all elements of a matrix.

    Args:
    matrix: must be a list of lists of integers or floats.
    div: can’t be equal to 0

    Returns:
    a new matrix

    Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
        : Each row of the matrix must have the same size
        : div must be a number
    ZeroDivisionError: division by zero
    """
    if not matrix or \
        not isinstance(matrix, list) or \
        not all(isinstance(i, list) for i in matrix) or \
        not all(len(j) for j in matrix) or \
        not all([all(isinstance(k, (int, float)) for k in m) for m in matrix]):

        message = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(message)
    # Checks if matrix is a list of lists of integers or floats

    check = [len(r) for r in matrix]

    if len(set(check)) != 1:
        message = "Each row of the matrix must have the same size"
        raise TypeError(message)
    # Check if each row of the matrix has the same size

    if not isinstance(div, (int, float)) or div != div:
        message = "div must be a number"
        raise TypeError(message)
    # Check if div is a number (integer or float)

    if div == 0:
        message = "division by zero"
        raise ZeroDivisionError(message)
    # Check if div is not equal to 0

    new_message = [[round(j / div, 2) for j in i] for i in matrix]
    return new_message
    # Divide each element of the matrix by div and round to 2 decimal places
