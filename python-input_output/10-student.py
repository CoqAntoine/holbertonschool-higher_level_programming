#!/usr/bin/python3
"""
Defines a Student class with JSON serialization and attribute filtering.
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.
        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {k: getattr(self, k)
                    for k in attrs if hasattr(self, k)}
        return self.__dict__
