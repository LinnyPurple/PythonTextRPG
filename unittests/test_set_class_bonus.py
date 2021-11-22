from unittest import TestCase
from game import make_character, set_class_bonus


class TestSetClassBonus(TestCase):
    def test_set_class_bonus_class(self):
        expected = {
            'class': 'Fighter',
            'name': '',
            'subclass': '',
            'level': 1,
            'stat_hp': 7,
            'stat_max_hp': 7,
            'stat_mp': 5,
            'stat_max_mp': 5,
            'stat_atk': 5,
            'stat_def': 2,
            'stat_mag': 2,
            'stat_mdf': 2,
            'stat_spd': 4,
            'stat_luk': 3,
            'skills': [],
            'items': {},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        class_type = 'class'
        character = make_character()
        character[class_type] = 'Fighter'
        set_class_bonus(character, class_type)
        actual = character
        self.assertEqual(expected, actual)

    def test_set_class_bonus_subclass(self):
        expected = {
            'class': '',
            'name': '',
            'subclass': 'Cleric',
            'level': 1,
            'stat_hp': 6,
            'stat_max_hp': 6,
            'stat_mp': 6,
            'stat_max_mp': 6,
            'stat_atk': 2,
            'stat_def': 2,
            'stat_mag': 3,
            'stat_mdf': 4,
            'stat_spd': 2,
            'stat_luk': 2,
            'skills': [],
            'items': {},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        class_type = 'subclass'
        character = make_character()
        character[class_type] = 'Cleric'
        set_class_bonus(character, class_type)
        actual = character
        self.assertEqual(expected, actual)
