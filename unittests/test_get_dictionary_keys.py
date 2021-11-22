from unittest import TestCase
from game import get_dictionary_keys


class TestGetDictionaryKeys(TestCase):
    def test_get_dictionary_keys_blank_dictionary(self):
        dictionary_list = []
        dictionary_key = 'a'
        expected = []
        actual = get_dictionary_keys(dictionary_list, dictionary_key)
        self.assertEqual(expected, actual)

    def test_get_dictionary_keys_one_entry(self):
        dictionary_list = [{'a': 2}]
        dictionary_key = 'a'
        expected = [2]
        actual = get_dictionary_keys(dictionary_list, dictionary_key)
        self.assertEqual(expected, actual)

    def test_get_dictionary_keys_many_entries(self):
        dictionary_list = [{'a': 2}, {'a': -3}, {'a': 'bee'}]
        dictionary_key = 'a'
        expected = [2, -3, 'bee']
        actual = get_dictionary_keys(dictionary_list, dictionary_key)
        self.assertEqual(expected, actual)
