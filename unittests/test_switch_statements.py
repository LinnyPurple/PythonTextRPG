from unittest import TestCase
from game import switch_statements


class TestSwitchStatements(TestCase):
    def test_switch_statements(self):
        expected = {
            'organ_man_1': False,
            'organ_man_2': False,
            'organ_man_final': False,
            'first_town_first_visit': False,
            'colorless_first_visit': False,
            'mountains_first_visit': False,
            'boss_1': False,
            'boss_2': False,
            'boss_3': False,
            'boss_final': False
        }
        actual = switch_statements()
        self.assertEqual(expected, actual)
