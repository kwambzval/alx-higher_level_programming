#!/usr/bin/python3
"""
This module contains a class 'MyInt' that inherits from 'int'.
"""


class MyInt(int):
    """
    This is the 'MyInt' class.

    This class includes inverted '==' and '!=' operators.
    """

    def __eq__(self, other):
        """
        This method inverts the '==' operator.

        Args:
            other: The object to compare with.

        Returns:
            True if self and other are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        This method inverts the '!=' operator.

        Args:
            other: The object to compare with.

        Returns:
            True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
