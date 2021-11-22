from unittest import TestCase
from game import get_color, print_color


class TestPrintColor(TestCase):
    def test_print_corner_no_color(self):
        row = -1
        column = -1
        expected = ""
        actual = print_color(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_beginning_area(self):
        row = 24
        column = 2
        expected = f"{get_color('c_white')}¤¤¤{get_color('c_reset')}"
        actual = print_color(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_first_area(self):
        row = 21
        column = 12
        expected = f"{get_color('c_magenta')}≡≡≡{get_color('c_reset')}"
        actual = print_color(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_second_area(self):
        row = 12
        column = 2
        expected = f"{get_color('c_yellow')}◊ð≈{get_color('c_reset')}"
        actual = print_color(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_third_area(self):
        row = 5
        column = 20
        expected = f"{get_color('c_cyan')}△Λ▴{get_color('c_reset')}"
        actual = print_color(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_main_area(self):
        row = 16
        column = 16
        expected = f"{get_color('c_green')}Îî↑{get_color('c_reset')}"
        actual = print_color(row, column)
        self.assertEqual(expected, actual)

    def test_print_corner_final_area(self):
        row = 0
        column = 7
        expected = f"{get_color('b_black')}{get_color('c_red')}Ξ♰Ψ{get_color('c_reset')}"
        actual = print_color(row, column)
        self.assertEqual(expected, actual)
