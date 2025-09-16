#!/usr/bin/python3
"""
This module defines a `Square` class that represents a geometric square.
It includes validation for the size and position attributes, and provides
methods to calculate the area and print the square.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        size (int): The length of a side of the square.
            Must be a non-negative integer.
        position (tuple): A tuple of 2 non-negative integers that represents
            the horizontal and vertical position when printing the square.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square with the character '#', considering
            the position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The length of a side of the square.
                Defaults to 0. Must be a non-negative integer.
            position (tuple, optional): A tuple of 2 non-negative integers.
                Defaults to (0, 0). Determines the position when printing.

        Raises:
            TypeError: If size is not an integer or position is not a tuple of
                2 non-negative integers.
            ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

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
            value (int): The new size of the square.
                Must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        tuple: Get or set the position of the square.
        Must be a tuple of 2 non-negative integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set a new position for the square.

        Args:
            value (tuple): A tuple of 2 non-negative integers representing
                the horizontal and vertical position when printing.

        Raises:
            TypeError: If value is not a tuple of 2 non-negative integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#'.

        The square is printed at the given position:
            - `position[1]` adds newlines before the square.
            - `position[0]` adds spaces before each row.
        If size is 0, an empty line is printed instead.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end='')
                print("#" * self.__size)
