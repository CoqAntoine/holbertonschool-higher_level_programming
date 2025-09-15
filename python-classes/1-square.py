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
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        Args:
            size (int): The length of a side of the square.
        """
        self.__size = size
