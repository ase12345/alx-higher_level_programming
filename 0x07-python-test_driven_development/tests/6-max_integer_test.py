#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([3]), 3)

    def test_negative_ints(self):
        self.assertEqual(max_integer([1, 3, 74, -2]), 74)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.4, 1.22, 3.4, 4.8, 4.5]), 4.8)
        self.assertEqual(max_integer([1.2, 3.3, 74.3, -2.9, 74.0]), 74.3)
        self.assertEqual(max_integer([1.2, 3.3, 74, -2.9, 73.0]), 74)
        self.assertEqual(max_integer([1.2, 3.3, 70, -2.9, 73.0]), 73.0)
        self.assertEqual(max_integer([-1.3, -1.2, -3.9, -4.2]), -1.2)

    def test_None(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([None]), None)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 3, 4])

    def test_no_param(self):
        self.assertEqual(max_integer(), None)

    def test_strings(self):
        self.assertEqual(max_integer("1, 3, 4"), "4")
        self.assertEqual(max_integer("143"), "4")
        self.assertEqual(max_integer(", ,"), ",")
        self.assertEqual(max_integer(", , 'ab' "), "b")
        self.assertEqual(max_integer("[], , 'ab' "), "b")

    def test_other_data_structs(self):
        self.assertEqual(max_integer(["abc"]), "abc")
        self.assertEqual(max_integer(["abc", "cds"]), "cds")
        self.assertEqual(max_integer(["abc", "1", "cds", "3", "5"]), "cds")
        self.assertEqual(max_integer([[1, 2, 3], [1, 3, 2]]), [1, 3, 2])
        self.assertEqual(max_integer((1, 2, 3, 9, 7)), 9)
        with self.assertRaises(KeyError):
            max_integer({1: 1, 2: 3, 3: 2})

    def test_mixed_list(self):
        with self.assertRaises(TypeError):
            max_integer(["abc", 1, "cds", 3.5, 5])
        with self.assertRaises(TypeError):
            max_integer(["abc", [1], "cds", 3.5, 5])
