#!/usr/bin/python3
"""
Unittest for Rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for Rectangle class."""

    def test_rectangle_creation(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_x_y(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with self.assertLogs() as captured:
            r.display()
        self.assertEqual(captured.output[-1].strip(), expected_output.strip())

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        r_dict = r.to_dictionary()
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r_dict, expected)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, width=5, height=5)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)


if __name__ == "__main__":
    unittest.main()
