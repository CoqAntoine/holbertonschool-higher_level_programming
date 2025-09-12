#!/usr/bin/python3
"""
Module square_printer

This module provides a function to print a square made of the '#' character
to the console.
"""


def print_square(size):
    """
    Prints a square made of the '#' character to the console.

    Args:
        size (int): The size of the square to print. Represents both the number
                    of rows and columns. Must be >= 0.

    Behavior:
        - If `size` is negative, prints an error message: "size must be >= 0"
        - If `size` is 0, prints nothing.
        - Prints a `size` x `size` square of '#' characters, each row followed
          by a newline.
    """
    if size == "" or size is None:
        raise TypeError("function need 1 argument")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print('#', end='')
        print()
