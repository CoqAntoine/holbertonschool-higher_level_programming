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

    skip_space = False  # Flag to skip one space after punctuation
    for char in text:
        if skip_space:
            skip_space = False
            if char == " ":
                continue  # Ignore the first space after punctuation

        if char in ".?:":
            print(char)
            print()  # extra newline to make 2 new lines total
            skip_space = True
        else:
            print(char, end="")