#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for the function max_integer"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_valid_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 8, -3, 5]), 8)
        self.assertEqual(max_integer([-1, -4, -7, -5]), -1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([5.1, 5.4, 5.3, 5.9, 5.6]), 5.9)
        self.assertEqual(max_integer((1, 3, 5, 6, 4)), 6)
        self.assertEqual(max_integer("1, 3, 5, 4, 2"), "5")
        self.assertEqual(max_integer("string"), "t")

    def test_exceptions_raised(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

        with self.assertRaises(TypeError):
            max_integer(5)

        with self.assertRaises(TypeError):
            max_integer([1, 5, [10], (6, 13)])
