from unittest import TestCase
from unittest.mock import patch
from game import set_class


class TestSetClass(TestCase):
    @patch('builtins.input', side_effect=['f'])
    def test_set_class_one_letter_valid_input(self, mock_input):
        subclass = False
        expected = 'Fighter'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_set_class_one_number_valid_input(self, mock_input):
        subclass = False
        expected = 'Knight'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Cleric'])
    def test_set_class_long_valid_input(self, mock_input):
        subclass = False
        expected = 'Cleric'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['', 'w'])
    def test_set_class_one_letter_valid_input_with_invalid_input(self, mock_input):
        subclass = False
        expected = 'Wizard'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['bad input', '5'])
    def test_set_class_one_number_valid_input_with_invalid_input(self, mock_input):
        subclass = False
        expected = 'Thief'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7', 'Robot'])
    def test_set_class_long_valid_input_with_invalid_input(self, mock_input):
        subclass = False
        expected = 'Robot'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['f'])
    def test_set_class_one_letter_valid_input_subclass(self, mock_input):
        subclass = True
        expected = 'Fighter'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_set_class_one_number_valid_input_subclass(self, mock_input):
        subclass = True
        expected = 'Knight'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Cleric'])
    def test_set_class_long_valid_input_subclass(self, mock_input):
        subclass = True
        expected = 'Cleric'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['', 'w'])
    def test_set_class_one_letter_valid_input_with_invalid_input_subclass(self, mock_input):
        subclass = True
        expected = 'Wizard'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['bad input', '5'])
    def test_set_class_one_number_valid_input_with_invalid_input_subclass(self, mock_input):
        subclass = True
        expected = 'Thief'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['7', 'Robot'])
    def test_set_class_long_valid_input_with_invalid_input_subclass(self, mock_input):
        subclass = True
        expected = 'Robot'
        actual = set_class(subclass)
        self.assertEqual(expected, actual)
