from unittest import TestCase
from unittest.mock import patch
from game import make_character, checkout
import io


class TestCheckout(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_checkout_not_enough_money(self, mock_output):
        character = make_character()
        buy_input = 'Dream Candy'
        expected = 'Sorry, . I can\'t give credit. Come back when you\'re a little...MMM...richer!\n'
        checkout(character, buy_input)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_checkout_add_item(self, mock_output):
        character = make_character()
        character['money'] = 10
        buy_input = 'Dream Candy'
        expected = f'You just bought a {buy_input}. Have a good day!\n'
        checkout(character, buy_input)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
