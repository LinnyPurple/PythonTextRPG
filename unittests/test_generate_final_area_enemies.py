from unittest import TestCase
from unittest.mock import patch
from game import get_enemy, generate_final_area_enemies


class TestGenerateFinalAreaEnemies(TestCase):
    @patch('random.randint', return_value=0)
    def test_generate_final_area_enemies_dream_hell(self, random_number_generator):
        expected = get_enemy('Dream Hell')
        actual = generate_final_area_enemies()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_generate_final_area_enemies_eerie_ghost(self, random_number_generator):
        expected = get_enemy('Eerie Ghost')
        actual = generate_final_area_enemies()
        self.assertEqual(expected, actual)
