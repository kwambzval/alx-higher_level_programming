#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    This function adds two integers or floats.
    If the arguments are not integers or floats, it raises a TypeError.
    If the arguments are floats, they are casted to integers.
    The function returns an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
