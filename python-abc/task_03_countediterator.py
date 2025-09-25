#!/usr/bin/python3
"""
Module: counted_iterator

This module defines a CountedIterator class that wraps a standard Python iterator.
It keeps track of the number of items that have been iterated over.
"""

class CountedIterator:
    """
    A custom iterator that counts how many items have been fetched.

    Attributes:
        iterator: The original iterator object created from an iterable.
        count (int): Number of items that have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object (list, tuple, set, etc.).
        """
        self.iterator = iter(iterable)
        self.count = 0


    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Raises:
            StopIteration: When there are no more items left in the iterator.
        """
        try:
            value = next(self.iterator)
            self.count += 1
            return value
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        Return the number of items that have been iterated over so far.

        Returns:
            int: The current count of fetched items.
        """
        return self.count
    
    def __iter__(self):
        return self
