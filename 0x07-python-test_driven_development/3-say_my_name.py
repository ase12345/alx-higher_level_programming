#!/usr/bin/python3
"""
This module defines say_my_name().
Raises:
    TypeError: if first_name or last_name is not a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is " + first_name + last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
