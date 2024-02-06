#!/usr/bin/python3
"""
Module for reading a text file (UTF8) and printing it to stdout.

This module contains a function, read_file, which reads a text file (UTF8)
and prints it to stdout. The filename is passed as a parameter to the function.
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
