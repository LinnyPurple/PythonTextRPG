from unittest import TestCase
from game import print_walls


class TestPrintWalls(TestCase):
    def test_print_walls_not_a_wall(self):
        row = 0
        column = 0
        expected = ""
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_up_down_wall(self):
        row = 20
        column = 25
        expected = "║"
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_up_down_wall_with_right_connector(self):
        row = 1
        column = -1
        expected = "╠"
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_left_right_wall_with_up_connector(self):
        row = 20
        column = 7
        expected = "═╩═"
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_up_down_wall_with_left_connector(self):
        row = 10
        column = 25
        expected = "╣"
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_left_right_wall(self):
        row = -1
        column = 12
        expected = "═══"
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_inner_up_down_wall(self):
        row = 16
        column = 7
        expected = " ║ "
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_inner_top_left_wall(self):
        row = 3
        column = 11
        expected = " ╔═"
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_inner_top_right_wall(self):
        row = 10
        column = 7
        expected = "═╗ "
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)

    def test_print_walls_inner_bottom_left_wall(self):
        row = 10
        column = 11
        expected = " ╚═"
        actual = print_walls(row, column)
        self.assertEqual(expected, actual)
