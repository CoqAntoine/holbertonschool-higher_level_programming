#!/usr/bin/python3
"""
This module defines a `Rectangle` class that represents a geometric rectangle.
It provides attributes for width and height with validation and can be extended
with additional methods for manipulating rectangles.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        width (int): The width of the rectangle. Must be a non-negative integer.
        height (int): The height of the rectangle. Must be a non-negative integer.

    Methods:
        (to be added later, e.g., area() to compute the area of the rectangle)
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle.
                Defaults to 0. Must be a non-negative integer.
            height (int, optional): The height of the rectangle.
                Defaults to 0. Must be a non-negative integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0..
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        int: Get or set the width of the rectangle.
        Must be a non-negative integer.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Set a new width for the rectangle.

        Args:
            value (int): The new width of the rectangle.
                Must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: Get or set the height of the rectangle.
        Must be a non-negative integer.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Set a new height for the rectangle.

        Args:
            value (int): The new height of the rectangle.
                Must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
