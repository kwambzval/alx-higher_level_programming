#!/usr/bin/python3
"""
Module for appending a string at the end of a text file (UTF8)
and returning the number of characters added.

This module contains a function, append_write, which appends a string at the
end of a text file (UTF8)
and returns the number of characters added.
The filename and the text to be appended
are passed as parameters to the function.
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append to the file

    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
