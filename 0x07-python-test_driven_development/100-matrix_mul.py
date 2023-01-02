#!/usr/bin/python3
"""
This module defines the function matrix_mul()
Raises:
    TypeError: if either matrix is not a list of numbers (int or float)
    ValueError: if either list is empty
    TypeError: if either matrix contains an element that is not a number
    TypeError: if each row of the matrix is not the same size (rectangle)
    ValueError: if the matrices cannot be multiplied
"""


def matrix_mul(m_a, m_b):
    """
    Returns the result of m_a * m_b
    """
    matErr = "{} must be a list"
    matEmptyErr = "{} can't be empty"
    matSizeErr = "each row of {} must should be of the same size"
    matContentErr = "{} should contain only integers or floats"
    if type(m_a) is not list:
        raise TypeError(matErr.format("m_a"))
    if type(m_b) is not list:
        raise TypeError(matErr.format("m_b"))
    if len(m_a) == 0 or type(m_a[0]) is list and len(m_a[0]) == 0:
        raise ValueError(matEmptyErr.format("m_a"))
    if len(m_b) == 0 or type(m_b[0]) is list and len(m_b[0]) == 0:
        raise ValueError(matEmptyErr.format("m_b"))
    size = -1
    for row in m_a:
        if type(row) is list:
            if size == -1:
                size = len(row)
            else:
                if size != len(row):
                    raise TypeError(matSizeErr.format("m_a"))
            for element in row:
                if type(element) is not int and type(element) is not float:
                    raise TypeError(matContentErr.format("m_a"))
        else:
            raise TypeError(matContentErr.format("m_a"))
    size = -1
    for row in m_b:
        if type(row) is list:
            if size == -1:
                size = len(row)
            else:
                if size != len(row):
                    raise TypeError(matSizeErr.format("m_b"))
            for element in row:
                if type(element) is not int and type(element) is not float:
                    raise TypeError(matContentErr.format("m_b"))
        else:
            raise TypeError(matContentErr.format("m_b"))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for col in m_b[0]] for row in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
