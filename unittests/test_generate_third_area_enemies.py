from unittest import TestCase
from unittest.mock import patch
from game import get_enemy, generate_third_area_enemies


class TestGenerateThirdAreaEnemies(TestCase):
    def test_generate_third_area_enemies_golden_ticket(self):
        row = 6
        column = 21
        expected = get_enemy('Golden Ticket')
        actual = generate_third_area_enemies(row, column)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_generate_first_area_enemies_after_organ_man_spider(self, random_number_generator):
        row = 6
        column = 20
        expected = get_enemy('Dream Bell')
        actual = generate_third_area_enemies(row, column)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_generate_first_area_enemies_after_organ_man_dream_cell(self, random_number_generator):
        row = 6
        column = 20
        expected = get_enemy('Mountain Lion')
        actual = generate_third_area_enemies(row, column)
        self.assertEqual(expected, actual)
