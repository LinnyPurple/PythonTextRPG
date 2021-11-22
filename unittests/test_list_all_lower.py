from unittest import TestCase
from game import list_all_lower


class TestListAllLower(TestCase):
    def test_list_all_lower_blank(self):
        string_list = []
        expected = []
        actual = list_all_lower(string_list)
        self.assertEqual(expected, actual)

    def test_list_all_lower_one_all_lower(self):
        string_list = ['hi']
        expected = ['hi']
        actual = list_all_lower(string_list)
        self.assertEqual(expected, actual)

    def test_list_all_lower_one_all_upper(self):
        string_list = ['GEORGE']
        expected = ['george']
        actual = list_all_lower(string_list)
        self.assertEqual(expected, actual)

    def test_list_all_lower_one_some_lower_some_upper(self):
        string_list = ['Christmas']
        expected = ['christmas']
        actual = list_all_lower(string_list)
        self.assertEqual(expected, actual)

    def test_list_all_lower_many_all_lower(self):
        string_list = ['words', 'can', 'be', 'confusing']
        expected = ['words', 'can', 'be', 'confusing']
        actual = list_all_lower(string_list)
        self.assertEqual(expected, actual)

    def test_list_all_lower_many_all_upper(self):
        string_list = ['DIAMONDS', 'ARE', 'FLEETING']
        expected = ['diamonds', 'are', 'fleeting']
        actual = list_all_lower(string_list)
        self.assertEqual(expected, actual)

    def test_list_all_lower_many_some_lower_some_upper(self):
        string_list = ['Do', 'yOu', 'thiNk', 'aboUT', 'thingS']
        expected = ['do', 'you', 'think', 'about', 'things']
        actual = list_all_lower(string_list)
        self.assertEqual(expected, actual)
