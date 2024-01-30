#!/usr/bin/python3
class LockedClass:
    """
    A class that only allows setting the attribute `first_name`
    """
    __slots__ = ['first_name']
