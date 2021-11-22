from unittest import TestCase
from unittest.mock import patch
from game import print_damage_output
import io


class TestPrintDamageOutput(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_damage_output_attacker_is_defender(self, mock_output):
        attacker = {'name': 'Alice'}
        defender = {'name': 'Alice'}
        damage = -2
        expected = f"{attacker['name']} heals {-1 * damage} points of damage!\n"
        print_damage_output(attacker, defender, damage)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_damage_output_attacker_is_not_defender(self, mock_output):
        attacker = {'name': 'Alice'}
        defender = {'name': 'Bob'}
        damage = 2
        expected = f"{attacker['name']} deals {damage} points of damage!\n"
        print_damage_output(attacker, defender, damage)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
