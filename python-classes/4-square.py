#!/usr/bin/python3
"""
This module defines a `Square` class that represents a geometric square.
It can be extended with attributes and methods for manipulating squares.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        size (int): The length of a side of the square.
        Must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The length of a side of the square.
                Defaults to 0. Must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        int: Get or set the size of the square.
        The value must be a non-negative integer.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Set a new size value for the square.

        Args:
            value (int): The new size of the square. Must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
 
    def area(self):
        """
        Calculate the area of a rectangle

        Args:
            size (int): The length of a side of the square.
        """
        return self.__size * self.__size
