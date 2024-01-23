#!/usr/bin/python3
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
        self.size = size

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

    def area(self):
        """
        Calculate the area of the Square instance.

        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2
