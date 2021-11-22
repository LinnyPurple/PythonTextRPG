from unittest import TestCase
from game import print_corner


class TestPrintCorner(TestCase):
    def test_print_corner_not_a_corner(self):
        row = 0
        column = 0
        expected = ""
        actual = print_corner(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_top_left_corner(self):
        row = -1
        column = -1
        expected = "╔"
        actual = print_corner(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_top_right_corner(self):
        row = -1
        column = 25
        expected = "╗"
        actual = print_corner(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_bottom_left_corner(self):
        row = 25
        column = -1
        expected = "╚"
        actual = print_corner(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_bottom_right_corner(self):
        row = 25
        column = 25
        expected = "╝"
        actual = print_corner(row, column)
        self.assertEqual(expected, actual)
