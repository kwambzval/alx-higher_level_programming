#!/usr/bin/python3
"""
Module for converting a JSON string to a Python object.

This module contains a function, from_json_string, which takes a JSON string
and returns the Python object represented by the string.
"""


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by
    a JSON string

    Args:
        my_str (str): The JSON string to convert to a Python object

    Returns:
        object: The Python object represented by the JSON string
    """
    return json.loads(my_str)
