#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test case for the max_integer function
    """

    def test_max_at_end(self):
        """
        Test with max value at the end of the list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """
        Test with max value at the beginning of the list
        """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """
        Test with max value in the middle of the list
        """
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative_number(self):
        """
        Test with one negative number in the list
        """
        self.assertEqual(max_integer([1, -4, 3, 2]), 3)

    def test_all_negative_numbers(self):
        """
        Test with all negative numbers in the list
        """
        self.assertEqual(max_integer([-1, -4, -3, -2]), -1)

    def test_single_element_list(self):
        """
        Test with a single element in the list
        """
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """
        Test with an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """
        Test with float numbers in the list
        """
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_types(self):
        """
        Test with mixed types in the list (integers and floats)
        """
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

