#!/usr/bin/python3
"""
Module: shapes

This module defines an abstract base class Shape and concrete subclasses Circle
and Rectangle.
It also provides a utility function to display information about shapes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.

    Defines the interface for computing area and perimeter.
    Any class inheriting from Shape must implement these methods.
    """

    @abstractmethod
    def area(self):
        """
        Compute the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape class.

    Attributes:
        __radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """
        Compute the area of the circle.

        Formula:
            π * r^2

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius * self.__radius

    def perimeter(self):
        """
        Compute the perimeter (circumference) of the circle.

        Formula:
            2 * π * r

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle shape class.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Formula:
            width * height

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.

        Formula:
            2 * (width + height)

        Returns:
            float: The perimeter of the rectangle.
        """
        return self.width * 2 + self.height * 2


def shape_info(value):
    """
    Print the area and perimeter of a given shape.

    Args:
        value (Shape): An instance of a class inheriting from Shape.

    Prints:
        Area and perimeter of the given shape.
    """
    A = value.area()
    P = value.perimeter()

    print("Area:", A)
    print("Perimeter:", P)
