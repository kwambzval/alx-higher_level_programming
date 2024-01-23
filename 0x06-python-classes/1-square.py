#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
The Square class includes a private instance attribute size.
"""


class Square:
    """
    This is a class that defines a square.
    """
    def __init__(self, size):
        """
        Initialize Square instance with size.

        Args:
            size: The size of the sides of the Square.
        """
        self.__size = size
