#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
The Square class includes a private instance attribute size, a
getter and setter for size, and methods for calculating the area
printing the square and Coordinates of a square.
"""


class Square:
    """
    This class defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize Square instance with size and position.

        Args:
            size (int): The size of the sides of the Square.
            Must be an integer.
            position (tuple): The position of the Square.
            Must be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the Square instance.

        Returns:
            int: The size of the sides of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the Square instance.

        Args:
            value (int): The size of the sides of the Square.
            Must be an integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the Square instance.

        Returns:
            tuple: The position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the Square instance.

        Args:
            value (tuple): The position of the Square.
            Must be a tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2 or
        type(value[0]) is not int or value[0] < 0 or
        type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate the area of the Square instance.

        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the Square instance with the character #.

        Prints an empty line if size is equal to 0.
        Uses position by using space.
        """
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
