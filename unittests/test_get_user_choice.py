from unittest import TestCase
from unittest.mock import patch
from game import make_character, get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['n'])
    def test_get_user_choice_direction_one_letter(self, mock_input):
        character = make_character()
        expected = 'n'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_get_user_choice_direction_one_number(self, mock_input):
        character = make_character()
        expected = '2'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['south'])
    def test_get_user_choice_direction_one_word(self, mock_input):
        character = make_character()
        expected = 'south'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['WEST'])
    def test_get_user_choice_direction_one_word_all_caps(self, mock_input):
        character = make_character()
        expected = 'west'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['bad input', '1'])
    def test_get_user_choice_direction_bad_input(self, mock_input):
        character = make_character()
        expected = '1'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4n', 'e'])
    def test_get_user_choice_direction_many_short_list(self, mock_input):
        character = make_character()
        expected = 'e'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['p'])
    def test_get_user_choice_pack_one_letter(self, mock_input):
        character = make_character()
        expected = 'p'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['6'])
    def test_get_user_choice_buy_one_number(self, mock_input):
        character = make_character()
        character['x'] = 2
        character['y'] = 22
        expected = '6'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['inn'])
    def test_get_user_choice_inn_bad_input_long_word(self, mock_input):
        character = make_character()
        character['x'] = 2
        character['y'] = 22
        expected = 'inn'
        actual = get_user_choice(character)
        self.assertEqual(expected, actual)
