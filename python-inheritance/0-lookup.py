#!/usr/bin/python3
"""
This module provides a simple utility function to inspect Python objects.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: List of attributes and methods of the object.
    """
    return dir(obj)
