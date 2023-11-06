#!/usr/bin/python3
"""
Contains the lookup function

This module provides the lookup function, which returns a list\
    of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names of the object.

    Example:
        >>> lookup("Hello")
        ['__add__', '__class__', '__contains__', ...]
    """
    return dir(obj)
