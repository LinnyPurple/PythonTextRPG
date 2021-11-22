from unittest import TestCase
from game import get_item


class TestGetItem(TestCase):
    def test_get_item_dream_candy(self):
        expected = {
            'item_name': 'Dream Candy',
            'item_description': 'Heals 10 HP.',
            'item_cost': 5,
            'item_boost': 10,
            'item_stat_boost': ['stat_hp']
        }
        actual = get_item('Dream Candy')
        self.assertEqual(expected, actual)

    def test_get_item_chocolate_sundae(self):
        expected = {
            'item_name': 'Chocolate Sundae',
            'item_description': 'Heals 30 MP.',
            'item_cost': 30,
            'item_boost': 30,
            'item_stat_boost': ['stat_mp']
        }
        actual = get_item('Chocolate Sundae')
        self.assertEqual(expected, actual)

    def test_get_item_super_candy(self):
        expected = {
            'item_name': 'Super Candy',
            'item_description': 'Boosts ATK, DEF, MAG, MDF, SPD, and LUK by 2.',
            'item_cost': 100,
            'item_boost': 2,
            'item_stat_boost': ['stat_atk', 'stat_def', 'stat_mag', 'stat_mdf', 'stat_spd', 'stat_luk']
        }
        actual = get_item('Super Candy')
        self.assertEqual(expected, actual)
