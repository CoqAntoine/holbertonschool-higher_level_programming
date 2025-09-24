#!/usr/bin/python3
"""
Module: verbose_list

This module defines a VerboseList class that extends the built-in list.
It prints notifications whenever items are added or removed.
"""


class VerboseList(list):
    """
    A subclass of list that prints messages when items are added or removed.
    """

    def append(self, item):
        """
        Add a single element to the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from an iterable,
        and print a message showing how many items were added.
        """
        count_before = len(self)
        super().extend(iterable)
        count_after = len(self)
        items_added = count_after - count_before
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of item from the list,
        printing a message before removal.
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            raise ValueError(f"[{item}] not found in the list.")

    def pop(self, index=-1):
        """
        Remove and return item at index (default last),
        printing a message before removal.
        """
        if not self:
            raise IndexError("pop from empty list")
        try:
            item = self[index]
        except IndexError:
            raise IndexError("pop index out of range")
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
