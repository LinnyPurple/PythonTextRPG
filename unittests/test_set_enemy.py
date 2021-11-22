from unittest import TestCase
from game import set_enemy


class TestSetEnemy(TestCase):
    def test_set_enemy_blank(self):
        expected = {
            'name': '',
            'stat_hp': 0,
            'stat_max_hp': 0,
            'stat_mp': 0,
            'stat_max_mp': 0,
            'stat_atk': 0,
            'stat_def': 0,
            'stat_mag': 0,
            'stat_mdf': 0,
            'stat_spd': 0,
            'stat_luk': 0,
            'skills': [],
            'exp': 0,
            'money': 0
        }
        actual = set_enemy('', 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0)
        self.assertEqual(expected, actual)
