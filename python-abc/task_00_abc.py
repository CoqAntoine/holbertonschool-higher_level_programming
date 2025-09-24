#!/usr/bin/python3
"""
Module: animals

This module defines an abstract base class Animal and two concrete subclasses:
Dog and Cat. The abstract class enforces that all subclasses
implement the sound() method.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    All subclasses must implement the sound() method.

    Methods:
        sound(): Abstract method to produce the animal's sound.
    """

    def __init__(self):
        """
        Initialize an Animal instance.
        For abstract base class, this does not set any attributes.
        """
        pass

    @abstractmethod
    def sound(self):
        """
        Abstract method to produce the animal's sound.

        Raises:
            NotImplementedError: If the subclass does not override this method.
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog.

    Inherits from Animal and implements the sound() method.
    """

    def sound(self):
        """
        Return the sound made by a dog.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat.

    Inherits from Animal and implements the sound() method.
    """

    def sound(self):
        """
        Return the sound made by a cat.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"
