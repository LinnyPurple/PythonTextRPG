from unittest import TestCase
from unittest.mock import patch
from game import make_character, get_color, print_choices
import io


class TestPrintChoices(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_choices_not_at_town(self, mock_output):
        character = make_character()
        choices_list = ['north', 'east', 'south', 'west', 'pack']
        color_string = 'c_blue'
        expected = f"1. ({get_color(color_string)}N{get_color('c_reset')})orth\n" \
                   f"2. ({get_color(color_string)}E{get_color('c_reset')})ast\n" \
                   f"3. ({get_color(color_string)}S{get_color('c_reset')})outh\n" \
                   f"4. ({get_color(color_string)}W{get_color('c_reset')})est\n" \
                   f"5. ({get_color(color_string)}P{get_color('c_reset')})ack\n"
        print_choices(character, choices_list, color_string)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_choices_at_town(self, mock_output):
        character = make_character()
        character['x'] = 2
        character['y'] = 22
        choices_list = ['north', 'east', 'south', 'west', 'pack', 'buy', 'inn']
        color_string = 'c_blue'
        expected = f"1. ({get_color(color_string)}N{get_color('c_reset')})orth\n" \
                   f"2. ({get_color(color_string)}E{get_color('c_reset')})ast\n" \
                   f"3. ({get_color(color_string)}S{get_color('c_reset')})outh\n" \
                   f"4. ({get_color(color_string)}W{get_color('c_reset')})est\n" \
                   f"5. ({get_color(color_string)}P{get_color('c_reset')})ack\n" \
                   f"6. ({get_color(color_string)}B{get_color('c_reset')})uy\n" \
                   f"7. ({get_color(color_string)}I{get_color('c_reset')})nn\n"
        print_choices(character, choices_list, color_string)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_choices_buy(self, mock_output):
        character = make_character()
        character['x'] = 2
        character['y'] = 22
        choices_list = ['dream Candy', 'water']
        color_string = 'c_green'
        expected = f"1. ({get_color(color_string)}D{get_color('c_reset')})ream Candy\t\t Cost: 5\n" \
                   f"\t- Heals 10 HP.\n" \
                   f"2. ({get_color(color_string)}W{get_color('c_reset')})ater\t\t\t\t Cost: 15\n" \
                   f"\t- Heals 10 MP.\n"
        print_choices(character, choices_list, color_string)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_choices_buy_mountains(self, mock_output):
        character = make_character()
        character['x'] = 24
        character['y'] = 3
        choices_list = ['vanilla Ice Cream', 'chocolate Sundae']
        color_string = 'c_green'
        expected = f"1. ({get_color(color_string)}V{get_color('c_reset')})anilla Ice Cream\t Cost: 12\n" \
                   f"\t- Heals 30 HP.\n" \
                   f"2. ({get_color(color_string)}C{get_color('c_reset')})hocolate Sundae\t Cost: 30\n" \
                   f"\t- Heals 30 MP.\n"
        print_choices(character, choices_list, color_string)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_choices_skills(self, mock_output):
        character = make_character()
        choices_list = ['Heal', 'Fire']
        color_string = 'c_red'
        expected = f"1. ({get_color(color_string)}H{get_color('c_reset')})eal\n" \
                   f"\t- Heals the player.\n\t- MP Cost: 2\n" \
                   f"2. ({get_color(color_string)}F{get_color('c_reset')})ire\n" \
                   f"\t- Burns the foe with fire.\n\t- MP Cost: 2\n"
        print_choices(character, choices_list, color_string)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_choices_one_item(self, mock_output):
        character = make_character()
        character['items'] = {'Dream Candy': 1}
        choices_list = ['dream Candy']
        color_string = 'c_cyan'
        expected = f"1. ({get_color(color_string)}D{get_color('c_reset')})ream Candy\t\t (1)\n" \
                   f"\t- Heals 10 HP.\n"
        print_choices(character, choices_list, color_string)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_choices_many_items(self, mock_output):
        character = make_character()
        character['items'] = {'Dream Candy': 1, 'Super Candy': 2, 'Vanilla Ice Cream': 5}
        choices_list = ['dream Candy', 'super Candy', 'vanilla Ice Cream']
        color_string = 'c_cyan'
        expected = f"1. ({get_color(color_string)}D{get_color('c_reset')})ream Candy\t\t (1)\n" \
                   f"\t- Heals 10 HP.\n" \
                   f"2. ({get_color(color_string)}S{get_color('c_reset')})uper Candy\t\t (2)\n" \
                   f"\t- Boosts ATK, DEF, MAG, MDF, SPD, and LUK by 2.\n" \
                   f"3. ({get_color(color_string)}V{get_color('c_reset')})anilla Ice Cream\t (5)\n" \
                   f"\t- Heals 30 HP.\n"
        print_choices(character, choices_list, color_string)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
