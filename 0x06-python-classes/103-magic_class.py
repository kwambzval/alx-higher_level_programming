#!/usr/bin/python3
"""
Module level docstring.
This module contains the MagicClass which
performs operations related to a circle.
"""

import math


class MagicClass:
    """
    Class level docstring.
    MagicClass represents a circle with a given radius.
    """

    def __init__(self, radius=0):
        """
        Method level docstring.
        Initialize MagicClass with the radius of a circle.
        Args:
            radius (int, float): The radius of the circle. Must be a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Method level docstring.
        Calculate the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Method level docstring.
        Calculate the circumference of the circle.
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
