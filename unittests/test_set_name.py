from unittest import TestCase
from unittest.mock import patch
from game import set_name


class TestSetName(TestCase):
    @patch('builtins.input', side_effect=['N'])
    def test_set_name_one_letter(self, mock_input):
        expected = 'N'
        actual = set_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['George'])
    def test_set_name_many_letters(self, mock_input):
        expected = 'George'
        actual = set_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['', 'player'])
    def test_set_name_one_blank_then_valid_name(self, mock_input):
        expected = 'player'
        actual = set_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['     ', 'Hero of the Universe'])
    def test_set_name_many_blanks_then_valid_name(self, mock_input):
        expected = 'Hero of the Universe'
        actual = set_name()
        self.assertEqual(expected, actual)
