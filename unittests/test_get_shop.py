from unittest import TestCase
from game import get_shop


class TestGetShop(TestCase):
    def test_get_shop_not_mountains(self):
        character = {'x': 0}
        expected = ['dream Candy', 'water']
        actual = get_shop(character)
        self.assertEqual(expected, actual)

    def test_get_shop_mountains(self):
        character = {'x': 24}
        expected = ['vanilla Ice Cream', 'chocolate Sundae']
        actual = get_shop(character)
        self.assertEqual(expected, actual)
