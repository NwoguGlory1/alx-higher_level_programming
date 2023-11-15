#!/usr/bin/pythoni3
""" Unittest for max_integer function """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """Class for unittest of max_integer function"""


    def test_max_integerlist(self):
        self.assertEqual(max_integer([1, 5, 8, 2]), 8)
        self.assertEqual(max_integer([-1, 0, -5, -4]), 0)
        self.assertEqual(max_integer([-1, -5, -8, -2]), -1)
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
