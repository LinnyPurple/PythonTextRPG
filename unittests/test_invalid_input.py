from unittest import TestCase
from unittest.mock import patch
from game import invalid_input
import io


class TestInvalidInput(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input_empty_string(self, mock_output):
        wanted_input = ''
        expected = 'Invalid input. Please enter one of ().\n'
        invalid_input(wanted_input)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input_one_option(self, mock_output):
        wanted_input = ' h'
        expected = 'Invalid input. Please enter one of (h).\n'
        invalid_input(wanted_input)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input_many_options(self, mock_output):
        wanted_input = '    abcd'
        expected = 'Invalid input. Please enter one of (a/b/c/d).\n'
        invalid_input(wanted_input)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
