from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_order_same(self):
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
            'items': {},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        actual = make_character()
        self.assertEqual(expected, actual)

    def test_make_character_order_different(self):
        expected = {
            'class': '',
            'name': '',
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
            'items': {},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        actual = make_character()
        self.assertEqual(expected, actual)
