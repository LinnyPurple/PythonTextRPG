from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.randint', return_value=0)
    def test_check_for_foes_foe_encountered(self, random_number_generator):
        expected = True
        actual = check_for_foes()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_check_for_foes_foe_not_encountered(self, random_number_generator):
        expected = False
        actual = check_for_foes()
        self.assertEqual(expected, actual)
