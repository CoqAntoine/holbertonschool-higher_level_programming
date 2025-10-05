#!/usr/bin/python3
"""
Module: task_01_pickle
======================

This module defines a `CustomObject` class that demonstrates
object serialization and deserialization using Python's `pickle` module.

The class includes:
- Attributes: name, age, is_student
- A display method to print its attributes
- Methods to serialize and deserialize instances safely

Example:
    >>> obj = CustomObject("John", 25, True)
    >>> obj.serialize("data.pkl")
    >>> loaded_obj = CustomObject.deserialize("data.pkl")
    >>> loaded_obj.display()
    Name: John
    Age: 25
    Is Student: True
"""

import pickle


class CustomObject:
    """
    A custom class representing a simple object with serialization support.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance and save it to a file.

        Args:
            filename (str): The name of the file where the object will be saved.

        Returns:
            bool: True if serialization succeeded, False otherwise.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except Exception:
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject | None: The deserialized object if successful,
                                 otherwise None.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
            return None
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        except Exception:
            return None
