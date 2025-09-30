#!/usr/bin/python3
"""
This module returns the dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure
    """
    new_dict = obj.__dict__
    return new_dict
