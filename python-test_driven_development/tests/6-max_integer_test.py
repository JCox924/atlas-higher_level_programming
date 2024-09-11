#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max value is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-2, 0, 3, -1, 2]), 3)

    def test_single_element(self):
        """Test with a single-element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Test with a mix of integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string(self):
        """Test with a string of characters."""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none_argument(self):
        """Test with None as an argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        """Test with a non-iterable argument."""
        with self.assertRaises(TypeError):
            max_integer(7)

    def test_list_with_none(self):
        """Test with a list containing None."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])

    def test_list_with_different_types(self):
        """Test with a list of mixed data types."""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

if __name__ == '__main__':
    unittest.main()
