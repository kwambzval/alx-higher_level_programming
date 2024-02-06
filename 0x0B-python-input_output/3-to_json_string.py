#!/usr/bin/python3
"""
Module for converting an object to a JSON representation.

This module contains a function, to_json_string, which takes an object
and returns the JSON representation of that object as a string.
"""


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)

    Args:
        my_obj: The object to convert to JSON

    Returns:
        str: The JSON representation of the object
    """
    return json.dumps(my_obj)
