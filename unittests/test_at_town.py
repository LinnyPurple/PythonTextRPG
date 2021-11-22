from unittest import TestCase
from game import make_character, at_town


class TestAtTown(TestCase):
    def test_at_town_list_false(self):
        character = make_character()
        options = ['north', 'east', 'south', 'west', 'pack']
        expected = ['north', 'east', 'south', 'west', 'pack']
        actual = at_town(character, options)
        self.assertEqual(expected, actual)

    def test_at_town_list_true(self):
        character = make_character()
        character['x'] = 2
        character['y'] = 22
        options = ['north', 'east', 'south', 'west', 'pack']
        expected = ['north', 'east', 'south', 'west', 'pack', 'buy', 'inn']
        actual = at_town(character, options)
        self.assertEqual(expected, actual)

    def test_at_town_string_false(self):
        character = make_character()
        options = '12345neswp'
        expected = '12345neswp'
        actual = at_town(character, options)
        self.assertEqual(expected, actual)

    def test_at_town_string_true(self):
        character = make_character()
        character['x'] = 24
        character['y'] = 3
        options = '12345neswp'
        expected = '1234567neswpbi'
        actual = at_town(character, options)
        self.assertEqual(expected, actual)
