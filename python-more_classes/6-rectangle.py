#!/usr/bin/python3
"""
This module defines a `Rectangle` class that represents a geometric rectangle.
It provides attributes for width and height with validation, and includes
methods to calculate the area and perimeter of the rectangle.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        width (int): The width of the rectangle.
            Must be a non-negative integer.
        height (int): The height of the rectangle.
            Must be a non-negative integer.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """
    number_of_instances = 0

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
        number_of_instances += 1

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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
                Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.height * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle using the '#' character

        Returns:
            str: The rectangle drawn with '#' characters.
                If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rows = []
        for _ in range(self.height):
            rows.append("#" * self.width)

        # Join rows with newlines
        return "\n".join(rows)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        number_of_instances -= 1
