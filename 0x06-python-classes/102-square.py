#!/usr/bin/python3
"""
This module contains a class Square that defines a square.
"""


class Square:
    """
    This class defines a square by its size, which is equal on all sides.
    """

    def __init__(self, size=0):
        """
        Initialize Square instance with size.
        Args:
            size (int, float): The size of the sides of the
            Square. Must be a number.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the Square instance.
        Returns:
            int, float: The size of the sides of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the Square instance.
        Args:
            value (int, float): The size of the sides
            of the Square. Must be a number.
        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the Square instance.
        Returns:
            float: The area of the Square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
