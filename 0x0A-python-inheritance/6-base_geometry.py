#!/usr/bin/python3
"""
This module contains a class 'BaseGeometry' with a method 'area'.
"""


class BaseGeometry:
    """
    This is the 'BaseGeometry' class.

    This class includes a method 'area' that raises an exception.
    """

    def area(self):
        """
        This method raises an exception.
        Raises:
            Exception: Always, with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
