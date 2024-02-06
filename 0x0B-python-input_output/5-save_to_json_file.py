#!/usr/bin/python3
"""
Module for writing an object to a text file using a JSON representation.

This module contains a function, save_to_json_file, which takes an object
and a filename, converts the object to a JSON string,
and writes it to the file.
"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to write to the file
        filename (str): The name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
