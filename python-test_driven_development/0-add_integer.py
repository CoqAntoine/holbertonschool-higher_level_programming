"""
This module provides a function to add two integers.
The function ensures type checking and casting of floats.
It raises a TypeError if arguments are not numbers.
Floats are cast to integers before addition.
The result is always returned as an integer.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats after type checking.
    Floats are cast to integers before addition.
    Returns the integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

