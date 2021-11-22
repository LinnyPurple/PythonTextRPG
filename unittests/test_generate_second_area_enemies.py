from unittest import TestCase
from unittest.mock import patch
from game import get_enemy, generate_second_area_enemies


class TestGenerateSecondAreaEnemies(TestCase):
    def test_generate_second_area_enemies_before_organ_man(self):
        row = 14
        expected = get_enemy('Dream Swell')
        actual = generate_second_area_enemies(row)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_generate_second_area_enemies_after_organ_man_spider(self, random_number_generator):
        row = 16
        expected = get_enemy('Floating Square')
        actual = generate_second_area_enemies(row)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_generate_second_area_enemies_after_organ_man_dream_cell(self, random_number_generator):
        row = 16
        expected = get_enemy('Dream Swell')
        actual = generate_second_area_enemies(row)
        self.assertEqual(expected, actual)
