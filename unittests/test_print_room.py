from unittest import TestCase
from game import get_color, make_character, print_room


class TestPrintRoom(TestCase):
    def test_print_room_not_a_room(self):
        row = -3
        column = -3
        character = make_character()
        expected = "   "
        actual = print_room(row, column, character)
        self.assertEqual(expected, actual)

    def test_print_room_initialize_player(self):
        row = 24
        column = 0
        character = make_character()
        expected = f"{get_color('c_blue')}<P>{get_color('c_reset')}"
        actual = print_room(row, column, character)
        self.assertEqual(expected, actual)

    def test_print_room_player_in_final_area(self):
        row = 0
        column = 0
        character = make_character()
        character['y'] = 0
        expected = f"{get_color('b_black')}{get_color('c_blue')}<P>{get_color('c_reset')}"
        actual = print_room(row, column, character)
        self.assertEqual(expected, actual)

    def test_print_room_is_corner(self):
        row = -1
        column = -1
        character = make_character()
        expected = "╔"
        actual = print_room(row, column, character)
        self.assertEqual(expected, actual)

    def test_print_room_is_wall(self):
        row = 20
        column = 25
        character = make_character()
        expected = "║"
        actual = print_room(row, column, character)
        self.assertEqual(expected, actual)

    def test_print_room_is_color(self):
        row = 24
        column = 2
        character = make_character()
        expected = f"{get_color('c_white')}¤¤¤{get_color('c_reset')}"
        actual = print_room(row, column, character)
        self.assertEqual(expected, actual)
