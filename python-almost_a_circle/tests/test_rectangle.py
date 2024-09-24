#!/usr/bin/python3
"""
Unittest for Rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle class."""

    def test_rectangle_initialization(self):
        """Test initialization of Rectangle with valid arguments."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rectangle_invalid_width(self):
        """Test if invalid width raises correct exception."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_rectangle_invalid_height(self):
        """Test if invalid height raises correct exception."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_rectangle_invalid_x(self):
        """Test if invalid x raises correct exception."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -5, 0)

    def test_rectangle_invalid_y(self):
        """Test if invalid y raises correct exception."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -5)

    def test_area(self):
        """Test the area calculation."""
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)


if __name__ == "__main__":
    unittest.main()
