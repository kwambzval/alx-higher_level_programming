#!/usr/bin/python3
"""
This module contains a class 'Square' that inherits from 'Rectangle'.
"""


class BaseGeometry:
    """
    This is the 'BaseGeometry' class.

    This class includes a method 'integer_validator' that validates values.
    """

    def integer_validator(self, name, value):
        """
        This method validates the value.

        Args:
            name: The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This is the 'Rectangle' class.

    This class includes private attributes 'width' and 'height',
    an 'area' method, and a '__str__' method.
    """

    def __init__(self, width, height):
        """
        This method initializes the 'Rectangle' instance.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This method returns the area of the rectangle.
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        This method returns a string representation of the rectangle.

        Returns:
            A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    This is the 'Square' class.

    This class includes a private attribute 'size'.
    """

    def __init__(self, size):
        """
        This method initializes the 'Square' instance.

        Args:
            size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        This method returns a string representation of the square.

        Returns:
            A string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
