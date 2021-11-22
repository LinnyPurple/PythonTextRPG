from unittest import TestCase
from game import make_character, use_item


class TestUseItem(TestCase):
    def test_use_item_one_item_once(self):
        character = make_character()
        character['items'] = {'Water': 2}
        item = 'Water'
        expected = {
            'name': '',
            'class': '',
            'subclass': '',
            'level': 1,
            'stat_hp': 5,
            'stat_max_hp': 5,
            'stat_mp': 5,
            'stat_max_mp': 5,
            'stat_atk': 2,
            'stat_def': 2,
            'stat_mag': 2,
            'stat_mdf': 2,
            'stat_spd': 2,
            'stat_luk': 2,
            'skills': [],
            'items': {'Water': 1},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        use_item(character, item)
        actual = character
        self.assertEqual(expected, actual)

    def test_use_item_one_item_many_times(self):
        character = make_character()
        character['items'] = {'Water': 3}
        item = 'Water'
        expected = {
            'name': '',
            'class': '',
            'subclass': '',
            'level': 1,
            'stat_hp': 5,
            'stat_max_hp': 5,
            'stat_mp': 5,
            'stat_max_mp': 5,
            'stat_atk': 2,
            'stat_def': 2,
            'stat_mag': 2,
            'stat_mdf': 2,
            'stat_spd': 2,
            'stat_luk': 2,
            'skills': [],
            'items': {'Water': 1},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        use_item(character, item)
        use_item(character, item)
        actual = character
        self.assertEqual(expected, actual)

    def test_use_item_many_items_once(self):
        character = make_character()
        character['items'] = {'Water': 1, 'Super Candy': 1}
        item = 'Water'
        expected = {
            'name': '',
            'class': '',
            'subclass': '',
            'level': 1,
            'stat_hp': 5,
            'stat_max_hp': 5,
            'stat_mp': 5,
            'stat_max_mp': 5,
            'stat_atk': 2,
            'stat_def': 2,
            'stat_mag': 2,
            'stat_mdf': 2,
            'stat_spd': 2,
            'stat_luk': 2,
            'skills': [],
            'items': {'Super Candy': 1},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        use_item(character, item)
        actual = character
        self.assertEqual(expected, actual)

    def test_use_item_many_items_many_times(self):
        character = make_character()
        character['items'] = {'Water': 2, 'Super Candy': 1}
        item_one = 'Water'
        item_two = 'Super Candy'
        expected = {
            'name': '',
            'class': '',
            'subclass': '',
            'level': 1,
            'stat_hp': 5,
            'stat_max_hp': 5,
            'stat_mp': 5,
            'stat_max_mp': 5,
            'stat_atk': 4,
            'stat_def': 4,
            'stat_mag': 4,
            'stat_mdf': 4,
            'stat_spd': 4,
            'stat_luk': 4,
            'skills': [],
            'items': {'Water': 1},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        use_item(character, item_one)
        use_item(character, item_two)
        actual = character
        self.assertEqual(expected, actual)
