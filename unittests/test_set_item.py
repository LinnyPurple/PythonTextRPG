from unittest import TestCase
from game import set_item


class TestSetItem(TestCase):
    def test_set_item_blank(self):
        expected = {
            'item_name': '',
            'item_description': '',
            'item_cost': 0,
            'item_boost': 0,
            'item_stat_boost': []
        }
        actual = set_item('', '', 0, 0, [])
        self.assertEqual(expected, actual)
