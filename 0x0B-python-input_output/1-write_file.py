#!/usr/bin/python3
"""
Module for writing a string to a text file (UTF8) and returning
the number of characters written.

This module contains a function, write_file, which writes a string
to a text file (UTF8) and returns the number of characters written.
The filename and the text to be written
are passed as parameters to the function.
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
