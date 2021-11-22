from unittest import TestCase
from game import make_character, add_skill


class TestAddSkill(TestCase):
    def test_add_skill_double_attack(self):
        character = make_character()
        fighter_dict = {
            'skill_name': 'Double Attack',
            'mp_use': 2,
            'atk_power': character['stat_atk'],
            'defense': 'stat_def',
            'multiplier': 3,
            'description': 'Does twice the damage.',
            'battle_text': 'attacks the enemy with a strong force'
        }
        expected = {
            'name': '',
            'class': '',
            'subclass': '',
            'level': 1,
            'stat_hp': 5,
            'stat_max_hp': 5,
            'stat_mp': 5,
            'stat_max_mp': 5,
            'stat_atk': 2,
            'stat_def': 2,
            'stat_mag': 2,
            'stat_mdf': 2,
            'stat_spd': 2,
            'stat_luk': 2,
            'skills': [fighter_dict],
            'items': {},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        add_skill(character, 'Double Attack')
        actual = character
        self.assertEqual(expected, actual)

    def test_add_skill_heal(self):
        character = make_character()
        cleric_dict = {
            'skill_name': 'Heal',
            'mp_use': 2,
            'atk_power': -int(20 + character['stat_mag'] / 4),
            'defense': 0,
            'multiplier': 1,
            'description': 'Heals the player.',
            'battle_text': 'casts Heal'
        }
        expected = {
            'name': '',
            'class': '',
            'subclass': '',
            'level': 1,
            'stat_hp': 5,
            'stat_max_hp': 5,
            'stat_mp': 5,
            'stat_max_mp': 5,
            'stat_atk': 2,
            'stat_def': 2,
            'stat_mag': 2,
            'stat_mdf': 2,
            'stat_spd': 2,
            'stat_luk': 2,
            'skills': [cleric_dict],
            'items': {},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        add_skill(character, 'Heal')
        actual = character
        self.assertEqual(expected, actual)
