#!/usr/bin/python3
"""
This module appends a string at the end of a text file
and return the number of character added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and return the number of character added.
    """
    with open(filename, "a") as f:
        nb_char = f.write(text)
    f.closed
    return nb_char
