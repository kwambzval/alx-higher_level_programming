#!/usr/bin/python3
"""
This module contains a class 'Rectangle' that inherits from 'BaseGeometry'.
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

    This class includes private attributes 'width' and 'height'.
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
