#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Instantiation:
        Rectangle(width, height)

    Args:
        width (int): The width of the rectangle (must be > 0).
        height (int): The height of the rectangle (must be > 0).

    Both width and height are validated as positive integers
    using BaseGeometry.integer_validator.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
