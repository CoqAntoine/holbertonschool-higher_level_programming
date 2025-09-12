#!/usr/bin/python3
"""
Module text_formatter

This module provides a function to print a text with proper indentation 
after certain punctuation marks (., ?, :).
"""


def text_indentation(text):
    """
    Prints the input text with a newline after '.', '?', or ':' characters.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_spaces = False
    for char in text:
        if skip_spaces:
            if char == " ":
                continue  # ignore consecutive spaces
            skip_spaces = False

        if char in ".?:":
            print(char)
            print()  # two new lines
            skip_spaces = True
        else:
            print(char, end="")
