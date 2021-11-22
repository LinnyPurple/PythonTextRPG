from unittest import TestCase
from game import make_character, level_up


class TestLevelUp(TestCase):
    def test_level_up_initialize_character(self):
        character = make_character()
        expected = False
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_cannot_level_up(self):
        character = make_character()
        character['exp'] = 5
        expected = False
        actual = level_up(character)
        self.assertEqual(expected, actual)

    def test_level_up_can_level_up(self):
        character = make_character()
        character['exp'] = 10
        expected = True
        actual = level_up(character)
        self.assertEqual(expected, actual)
