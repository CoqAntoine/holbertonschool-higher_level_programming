#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class.

    Public Methods:
        area(): Raises an Exception indicating the method is not implemented.
    """

    def area(self):
        """
        Raises:
            Exception: Always raises an exception indicating that the area
            method is not implemented.
        """
        raise Exception("area() is not implemented")
