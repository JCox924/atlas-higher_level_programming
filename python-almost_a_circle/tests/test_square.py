#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class"""

    def test_square_creation(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 12)
        s_dict = s.to_dictionary()
        expected = {'id': 12, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s_dict, expected)

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=5, x=1, y=2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)


if __name__ == '__main__':
    unittest.main()
