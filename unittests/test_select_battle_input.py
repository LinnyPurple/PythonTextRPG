from unittest import TestCase
from unittest.mock import patch
from game import make_character, select_battle_input


class Test(TestCase):
    @patch('builtins.input', side_effect=['a'])
    def test_select_battle_input_one_letter(self, mock_input):
        character = make_character()
        expected = 'Attack'
        actual = select_battle_input(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_select_battle_input_one_number(self, mock_input):
        character = make_character()
        expected = 'Skill'
        actual = select_battle_input(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['item'])
    def test_select_battle_input_one_word(self, mock_input):
        character = make_character()
        expected = 'Item'
        actual = select_battle_input(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['bbbb', 'f'])
    def test_select_battle_input_invalid_input_then_one_letter(self, mock_input):
        character = make_character()
        expected = 'Flee'
        actual = select_battle_input(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['', '1'])
    def test_select_battle_input_invalid_input_then_one_number(self, mock_input):
        character = make_character()
        expected = 'Attack'
        actual = select_battle_input(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['skil', 'Skill'])
    def test_select_battle_input_invalid_input_then_one_word(self, mock_input):
        character = make_character()
        expected = 'Skill'
        actual = select_battle_input(character)
        self.assertEqual(expected, actual)
