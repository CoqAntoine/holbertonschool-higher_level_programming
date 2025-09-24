#!/usr/bin/python3
"""
This module defines the BaseGeometry class with unimplemented area
and a method to validate integer values.
"""


class BaseGeometry:
    """
    BaseGeometry class.

    Public Methods:
        area(): Raises an Exception indicating the method is not implemented.
        integer_validator(name, value): Validates that value is an integer.
    """

    def area(self):
        """
        Raises:
            Exception: Always raises an exception indicating that the area
            method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the variable to use in exception messages.
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
