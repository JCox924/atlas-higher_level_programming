#!/usr/bin/python3
"""
Unittest for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for Base class."""

    def test_id_auto_increment(self):
        """Test if id is auto-incremented when no id is provided."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_manual(self):
        """Test if id is manually assigned when provided."""
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_id_mixed(self):
        """Test both manual and auto-increment id assignment."""
        b1 = Base(50)
        b2 = Base()
        b3 = Base(10)
        b4 = Base()
        self.assertEqual(b1.id, 50)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 2)


if __name__ == "__main__":
    unittest.main()
