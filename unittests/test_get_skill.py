from unittest import TestCase
from game import make_character, get_enemy, get_skill


class TestGetSkill(TestCase):
    def test_get_skill_double_attack(self):
        character = make_character()
        expected = {
            'skill_name': 'Double Attack',
            'mp_use': 2,
            'atk_power': character['stat_atk'],
            'defense': 'stat_def',
            'multiplier': 3,
            'description': 'Does twice the damage.',
            'battle_text': 'attacks the enemy with a strong force'
        }
        actual = get_skill(character, 'Double Attack')
        self.assertEqual(expected, actual)

    def test_get_skill_bounce(self):
        enemy = get_enemy('Dream Cell')
        expected = {
            'skill_name': 'Bounce',
            'mp_use': 0,
            'atk_power': enemy['stat_atk'],
            'defense': 'stat_def',
            'multiplier': 2.5,
            'description': 'Bounce on the enemy.',
            'battle_text': 'bounces high and falls down'
        }
        actual = get_skill(enemy, 'Bounce')
        self.assertEqual(expected, actual)
