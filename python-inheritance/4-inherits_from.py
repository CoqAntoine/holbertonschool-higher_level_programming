#!/usr/bin/python3
"""
This module provides functions to check the type or class of an object,
including inheritance relationships.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherits
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
