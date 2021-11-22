from unittest import TestCase
from game import make_character, initialize_class_skills


class TestInitializeClassSkills(TestCase):
    def test_initialize_class_skills_class_thief_subclass_wizard(self):
        character = make_character()
        character['class'] = 'Thief'
        character['subclass'] = 'Wizard'
        thief_dict = {
            'skill_name': 'Critical Slash',
            'mp_use': 3,
            'atk_power': character['stat_atk'],
            'defense': 'stat_def',
            'multiplier': 2 + character['stat_luk'] / 10,
            'description': 'An attack that increases with the user\'s luck.',
            'battle_text': 'slashes the enemy with a critical blow'
        }
        wizard_dict = {
            'skill_name': 'Fire',
            'mp_use': 2,
            'atk_power': int(20 + character['stat_mag'] / 4),
            'defense': 'stat_mdf',
            'multiplier': 1,
            'description': 'Burns the foe with fire.',
            'battle_text': 'casts Fire'
        }
        expected = {
            'name': '',
            'class': 'Thief',
            'subclass': 'Wizard',
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
            'skills': [thief_dict, wizard_dict],
            'items': {},
            'exp': 0,
            'money': 0,
            'x': 0,
            'y': 24
        }
        initialize_class_skills(character)
        actual = character
        self.assertEqual(expected, actual)
