from unittest import TestCase
from game import make_character, get_skill, get_defense


class TestGetDefense(TestCase):
    def test_get_defense_string_defense(self):
        character = make_character()
        skill = get_skill(character, 'Fire')
        enemy = {'stat_mdf': 2}
        expected = 2
        actual = get_defense(enemy, skill)
        self.assertEqual(expected, actual)

    def test_get_defense_zero_defense(self):
        character = make_character()
        skill = get_skill(character, 'Heal')
        expected = 0
        actual = get_defense(character, skill)
        self.assertEqual(expected, actual)
