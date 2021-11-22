from unittest import TestCase
from game import get_color


class TestGetColor(TestCase):
    def test_get_color_reset_text_color(self):
        expected = '\033[0m'
        actual = get_color('c_reset')
        self.assertEqual(expected, actual)

    def test_get_color_background_color_black(self):
        expected = '\033[40m'
        actual = get_color('b_black')
        self.assertEqual(expected, actual)

    def test_get_color_text_color_blue(self):
        expected = '\033[94m'
        actual = get_color('c_blue')
        self.assertEqual(expected, actual)
