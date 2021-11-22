from unittest import TestCase
from game import convert_short_input


class TestConvertShortInput(TestCase):
    def test_convert_short_input_no_options(self):
        player_input = ''
        short_input = ''
        long_input = []
        expected = ''
        actual = convert_short_input(player_input, short_input, long_input)
        self.assertEqual(expected, actual)

    def test_convert_short_input_one_option_one_letter_input(self):
        player_input = 'a'
        short_input = '1a'
        long_input = ['Alice']
        expected = 'Alice'
        actual = convert_short_input(player_input, short_input, long_input)
        self.assertEqual(expected, actual)

    def test_convert_short_input_one_option_one_number_input(self):
        player_input = '1'
        short_input = '1a'
        long_input = ['Alice']
        expected = 'Alice'
        actual = convert_short_input(player_input, short_input, long_input)
        self.assertEqual(expected, actual)

    def test_convert_short_input_one_option_long_input(self):
        player_input = 'Alice'
        short_input = '1a'
        long_input = ['Alice']
        expected = 'Alice'
        actual = convert_short_input(player_input, short_input, long_input)
        self.assertEqual(expected, actual)

    def test_convert_short_input_many_options_one_letter_input(self):
        player_input = 'b'
        short_input = '123abc'
        long_input = ['Alice', 'Bob', 'Carol']
        expected = 'Bob'
        actual = convert_short_input(player_input, short_input, long_input)
        self.assertEqual(expected, actual)

    def test_convert_short_input_many_options_one_number_input(self):
        player_input = '3'
        short_input = '123abc'
        long_input = ['Alice', 'Bob', 'Carol']
        expected = 'Carol'
        actual = convert_short_input(player_input, short_input, long_input)
        self.assertEqual(expected, actual)

    def test_convert_short_input_many_options_long_input(self):
        player_input = 'Carol'
        short_input = '123abc'
        long_input = ['Alice', 'Bob', 'Carol']
        expected = 'Carol'
        actual = convert_short_input(player_input, short_input, long_input)
        self.assertEqual(expected, actual)
