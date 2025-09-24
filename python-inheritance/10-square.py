#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Instantiation:
        Square(size)

    Args:
        size (int): The size of the square (must be > 0).

    The size is validated as a positive integer using
    BaseGeometry.integer_validator (inherited via Rectangle).
    """

    def __init__(self, size):
        """
        Initialize a square with a given size.

        Args:
            size (int): The length of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size <= 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
