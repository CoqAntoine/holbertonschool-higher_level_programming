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
    do_not_space = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for character in text:
        if do_not_space and character == ' ':
            do_not_space = False
            continue
        if character == '.' or character == '?' or character == ':':
            print(character)
            do_not_space = True
        else:
            print(character, end="")
