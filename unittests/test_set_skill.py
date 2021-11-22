from unittest import TestCase
from game import set_skill


class TestSetSkill(TestCase):
    def test_set_skill_blank(self):
        expected = {
            'skill_name': '',
            'mp_use': 0,
            'atk_power': 0,
            'defense': 0,
            'multiplier': 0,
            'description': '',
            'battle_text': ''
        }
        actual = set_skill('', 0, 0, 0, 0, '', '')
        self.assertEqual(expected, actual)
