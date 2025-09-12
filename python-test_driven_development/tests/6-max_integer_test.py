#!/usr/bin/python3
"""Unittests for max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 10, 3, 4]), 10)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string(self):
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_empty_string(self):
        self.assertIsNone(max_integer(""))

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 123456789]), 123456789)


if __name__ == "__main__":
    unittest.main()
