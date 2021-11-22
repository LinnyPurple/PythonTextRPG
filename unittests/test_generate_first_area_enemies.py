from unittest import TestCase
from unittest.mock import patch
from game import get_enemy, generate_first_area_enemies


class Test(TestCase):
    def test_generate_first_area_enemies_before_organ_man(self):
        column = 6
        expected = get_enemy('Dream Cell')
        actual = generate_first_area_enemies(column)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_generate_first_area_enemies_after_organ_man_spider(self, random_number_generator):
        column = 15
        expected = get_enemy('Spider')
        actual = generate_first_area_enemies(column)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_generate_first_area_enemies_after_organ_man_dream_cell(self, random_number_generator):
        column = 15
        expected = get_enemy('Dream Cell')
        actual = generate_first_area_enemies(column)
        self.assertEqual(expected, actual)
