from unittest import TestCase
from unittest.mock import patch
from game import make_character, select_item


class TestSelectItem(TestCase):
    @patch('builtins.input', side_effect=[])
    def test_select_item_empty_pack(self, mock_input):
        character = make_character()
        character['items'] = {}
        expected = None
        actual = select_item(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['d'])
    def test_select_item_one_item_one_letter_input(self, mock_input):
        character = make_character()
        character['items'] = {'Dream Candy': 1}
        expected = 'Dream Candy'
        actual = select_item(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_select_item_one_item_one_number_input(self, mock_input):
        character = make_character()
        character['items'] = {'Dream Candy': 1, 'Super Candy': 2}
        expected = 'Super Candy'
        actual = select_item(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Super Candy'])
    def test_select_item_one_item_one_word_input(self, mock_input):
        character = make_character()
        character['items'] = {'Dream Candy': 1, 'Super Candy': 2}
        expected = 'Super Candy'
        actual = select_item(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    def test_select_item_one_item_invalid_input(self, mock_input):
        character = make_character()
        character['items'] = {'Vanilla Ice Cream': 1}
        expected = None
        actual = select_item(character)
        self.assertEqual(expected, actual)
