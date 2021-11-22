from unittest import TestCase
from game import convert_direction_choice


class Test(TestCase):
    def test_convert_direction_choice_one_letter_direction(self):
        dir_input = '1'
        expected = (0, -1)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_number_direction(self):
        dir_input = 'e'
        expected = (1, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_word_direction(self):
        dir_input = 'south'
        expected = (0, 1)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_letter_pack(self):
        dir_input = 'p'
        expected = (5, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_number_pack(self):
        dir_input = '5'
        expected = (5, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_word_pack(self):
        dir_input = 'pack'
        expected = (5, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_letter_buy(self):
        dir_input = 'b'
        expected = (6, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_number_buy(self):
        dir_input = '6'
        expected = (6, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_word_buy(self):
        dir_input = 'buy'
        expected = (6, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_letter_inn(self):
        dir_input = 'i'
        expected = (0, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_number_inn(self):
        dir_input = '7'
        expected = (0, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)

    def test_convert_direction_choice_one_word_inn(self):
        dir_input = 'inn'
        expected = (0, 0)
        actual = convert_direction_choice(dir_input)
        self.assertEqual(expected, actual)
