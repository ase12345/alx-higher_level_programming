#!/usr/bin/python3
"""
This module defines the function matrix_divided()
Raises:
    TypeError: if matrix is not a list of lists of numbers (int or float)
    TypeError: if each row of the matrix is not the same size
    TypeError: if div is not a number (int or float)
    ZeroDivisionError: if div is zero
"""


def matrix_divided(matrix, div):
    """
    Returns a matrix of the division of all elements in a matrix
    """
    matErr = "matrix must be a matrix (list of lists) of integers/floats"
    matSizeErr = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(matErr)
    size = -1
    for row in matrix:
        if type(row) is list:
            if size == -1:
                size = len(row)
            else:
                if size != len(row):
                    raise TypeError(matSizeErr)
            for element in row:
                if type(element) is not int and type(element) is not float:
                    raise TypeError(matErr)
        else:
            raise TypeError(matErr)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
