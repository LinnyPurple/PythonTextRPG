from unittest import TestCase
from game import make_character, move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        character = make_character()
        dir_input = 'n'
        expected_x = 0
        expected_y = 23
        move_character(character, dir_input)
        actual_x = character['x']
        actual_y = character['y']
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_character_east(self):
        character = make_character()
        dir_input = 'east'
        expected_x = 1
        expected_y = 24
        move_character(character, dir_input)
        actual_x = character['x']
        actual_y = character['y']
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_character_south(self):
        character = make_character()
        dir_input = '3'
        character['y'] = 23
        expected_x = 0
        expected_y = 24
        move_character(character, dir_input)
        actual_x = character['x']
        actual_y = character['y']
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_move_character_west(self):
        character = make_character()
        dir_input = 'west'
        character['x'] = 1
        expected_x = 0
        expected_y = 24
        move_character(character, dir_input)
        actual_x = character['x']
        actual_y = character['y']
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)
