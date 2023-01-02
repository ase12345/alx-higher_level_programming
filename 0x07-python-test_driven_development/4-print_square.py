#!/usr/bin/python3
"""
Module defines function print_square()
Raises:
        TypeError: if size is not an integer
        ValueError: if size is negative
"""


def print_square(size):
    """
    Prints a square of given size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("{}\n".format("#" * size) * size, end="")
