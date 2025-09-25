"""
Module: dragon_with_mixins

This module demonstrates the use of mixins in Python to compose
behaviors in a modular way. Two mixins are defined (SwimMixin and FlyMixin),
and a Dragon class inherits from both, showing that it can both swim and fly.

Classes:
    SwimMixin: Provides swimming behavior.
    FlyMixin: Provides flying behavior.
    Dragon: Combines SwimMixin and FlyMixin, and adds dragon-specific behavior.
"""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        """Print a message indicating that the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        """Print a message indicating that the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon that can both swim and fly, thanks to mixins."""

    def roar(self):
        """Print a message indicating that the dragon is roaring."""
        print("The dragon roars!")
