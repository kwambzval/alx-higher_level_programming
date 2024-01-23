#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
The Square class includes a private instance attribute size,
a getter and setter for size, and a method for calculating the area.
"""


class Square:
    """
    This is a class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initialize Square instance with size.

        Args:
            size: The size of the sides of the Square. Must be an integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculate the area of the Square instance.

        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2
