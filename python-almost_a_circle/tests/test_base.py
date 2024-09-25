#!/usr/bin/python3
"""
Unittest for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for Base class."""

    def test_id_auto_assign(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id)

    def test_id_manual(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]),
                         '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'),
                         [{'id': 89}])


if __name__ == "__main__":
    unittest.main()
