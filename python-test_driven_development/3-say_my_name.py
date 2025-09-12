#!/usr/bin/python3
"""
This module provides a simple function to print a full name.

The function `say_my_name` takes a first name and an optional last name,
validates their types, and prints the formatted full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the message "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to display.
        last_name (str, optional): The last name to display.
            Defaults to an empty string.

    Raises:
        TypeError: If `first_name` is not a string.
        TypeError: If `last_name` is not a string.
    """
    if first_name == "" or first_name is None:
        raise TypeError("say_my_name() missing 1 " \
        "required argument: 'first_name'")
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
