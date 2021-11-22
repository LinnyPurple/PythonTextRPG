from unittest import TestCase
from game import make_character, is_wall


class TestIsWall(TestCase):
    def test_is_wall_not_a_wall(self):
        row = 2
        column = 3
        character = make_character()
        expected = False
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)

    def test_is_wall_top_left_wall(self):
        row = -1
        column = -1
        character = make_character()
        expected = True
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)

    def test_is_wall_top_right_wall(self):
        row = -1
        column = 25
        character = make_character()
        expected = True
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)

    def test_is_wall_bottom_left_wall(self):
        row = 25
        column = -1
        character = make_character()
        expected = True
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)

    def test_is_wall_bottom_right_wall(self):
        row = 25
        column = 25
        character = make_character()
        expected = True
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)

    def test_is_wall_up_down_wall(self):
        row = 0
        column = 25
        character = make_character()
        expected = True
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)

    def test_is_wall_left_right_wall_with_up_connector(self):
        row = 20
        column = 7
        character = make_character()
        expected = True
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)

    def test_is_wall_left_right_wall(self):
        row = 20
        column = 8
        character = make_character()
        expected = True
        actual = is_wall(row, column, character)
        self.assertEqual(expected, actual)
