from unittest import TestCase
from game import list_to_string_by_first_letter


class TestListToStringByFirstLetter(TestCase):
    def test_list_to_string_by_first_letter_blank(self):
        string_list = []
        expected = ''
        actual = list_to_string_by_first_letter(string_list)
        self.assertEqual(expected, actual)

    def test_list_to_string_by_first_letter_one_element(self):
        string_list = ['computers']
        expected = '1c'
        actual = list_to_string_by_first_letter(string_list)
        self.assertEqual(expected, actual)

    def test_list_to_string_by_first_letter_many_elements(self):
        string_list = ['blue', 'red', 'yellow']
        expected = '123bry'
        actual = list_to_string_by_first_letter(string_list)
        self.assertEqual(expected, actual)