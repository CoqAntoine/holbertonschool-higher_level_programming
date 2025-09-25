"""
Module: flying_fish

This module demonstrates multiple inheritance in Python by defining
three classes: Fish, Bird, and FlyingFish. It shows how a subclass
can inherit behaviors from more than one parent class and override
their methods to provide customized functionality.

Classes:
    Fish: Represents a fish with swimming ability and aquatic habitat.
    Bird: Represents a bird with flying ability and aerial habitat.
    FlyingFish: A hybrid class that inherits from both Fish and Bird,
                demonstrating multiple inheritance and method overriding.
"""


class Fish:
    """Represents a fish with swimming ability and aquatic habitat."""

    def swim(self):
        """Print a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message about the fish's natural habitat (water)."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying ability and aerial habitat."""

    def fly(self):
        """Print a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message about the bird's natural habitat (sky)."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that can both swim and fly.

    This class demonstrates multiple inheritance by extending
    both the Fish and Bird classes. It overrides their methods
    to provide specialized behavior for a flying fish.
    """

    def fly(self):
        """Print a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a message about the flying fish's dual habitat."""
        print("The flying fish lives both in water and the sky!")
