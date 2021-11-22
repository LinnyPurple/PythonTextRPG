from unittest import TestCase
from unittest.mock import patch
from game import get_enemy, generate_main_area_enemies


class TestGenerateMainAreaEnemies(TestCase):
    @patch('random.randint', return_value=1)
    def test_generate_main_area_enemies_dream_cell(self, random_number_generator):
        expected = get_enemy('Dream Cell')
        actual = generate_main_area_enemies()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_generate_main_area_enemies_spider(self, random_number_generator):
        expected = get_enemy('Spider')
        actual = generate_main_area_enemies()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=7)
    def test_generate_main_area_enemies_dream_shell(self, random_number_generator):
        expected = get_enemy('Dream Shell')
        actual = generate_main_area_enemies()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=9)
    def test_generate_main_area_enemies_giant_moth(self, random_number_generator):
        expected = get_enemy('Giant Moth')
        actual = generate_main_area_enemies()
        self.assertEqual(expected, actual)
