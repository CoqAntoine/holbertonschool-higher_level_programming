#!/usr/bin/python3
"""
This module writes a string to a text file and
return the number of character written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and
    return the number of character written.
    """
    with open(filename, "w") as f:
        nb_char = f.write(text)
    f.closed
    return nb_char
