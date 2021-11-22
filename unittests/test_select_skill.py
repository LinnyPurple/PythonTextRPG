from unittest import TestCase
from unittest.mock import patch
from game import make_character, add_skill, select_skill
import io


class TestSelectSkill(TestCase):
    @patch('builtins.input', side_effect=['BAD SKILL'])
    def test_select_skill_cleric_knight_invalid_input(self, mock_input):
        character = make_character()
        add_skill(character, 'Heal')
        add_skill(character, 'Sword Of Light')
        expected = None
        actual = select_skill(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['h'])
    def test_select_skill_cleric_knight_heal_one_letter(self, mock_input):
        character = make_character()
        add_skill(character, 'Heal')
        add_skill(character, 'Sword Of Light')
        expected = 'Heal'
        actual = select_skill(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_select_skill_cleric_knight_heal_one_number(self, mock_input):
        character = make_character()
        add_skill(character, 'Heal')
        add_skill(character, 'Sword Of Light')
        expected = 'Sword Of Light'
        actual = select_skill(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Heal'])
    def test_select_skill_cleric_knight_heal_one_number(self, mock_input):
        character = make_character()
        add_skill(character, 'Heal')
        add_skill(character, 'Sword Of Light')
        expected = 'Heal'
        actual = select_skill(character)
        self.assertEqual(expected, actual)
