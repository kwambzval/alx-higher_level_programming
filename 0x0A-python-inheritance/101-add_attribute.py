#!/usr/bin/python3
"""
This module contains a function 'add_attribute' that adds a new
attribute to an object if possible.
"""


def add_attribute(obj, name, value):
    """
    Function to add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        name: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
