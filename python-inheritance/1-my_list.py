#!/usr/bin/python3
"""
This module provides a class that inherit from list.
"""


class MyList(list):
    """
    MyList class that inherits from the built-in list.

    Public Methods:
        print_sorted(): Prints the list elements sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.

        Assumption:
            All elements in the list are integers.
        """
        print(sorted(self))
