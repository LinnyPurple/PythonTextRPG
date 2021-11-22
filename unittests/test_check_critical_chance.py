from unittest import TestCase
from unittest.mock import patch
from game import check_critical_chance


class TestCheckCriticalChance(TestCase):
    @patch('random.random', return_value=0.5)
    def test_check_critical_chance_critical_hit(self, random_number_generator):
        expected = 1.75
        actual = check_critical_chance(0)
        self.assertEqual(expected, actual)

    def test_check_critical_chance_no_critical_hit(self):
        expected = 1
        actual = check_critical_chance(4)
        self.assertEqual(expected, actual)
