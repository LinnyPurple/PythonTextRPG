from unittest import TestCase
from unittest.mock import patch
from game import make_character, set_class_bonus, print_character_stats
import io


class TestPrintCharacterStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stats_initial(self, mock_output):
        character = make_character()
        stat_length = 14  # Stats are printed as two on each line, 19 characters total
        longest_string = max(len(character['name']), stat_length) + 9
        border = "#" + "=" * longest_string + "#"
        middle_border = "-" * (longest_string + 2)
        expected = f"\n{border}\n"\
                   f"Name:     {character['name']}\n"\
                   f"Class:    {character['class']}\n"\
                   f"Subclass: {character['subclass']}\n"\
                   f"{middle_border}\n"\
                   f"Level: {character['level']:18d}\n"\
                   f"Exp:   {character['exp']:18d}\n"\
                   f"Money: {character['money']:18d}\n"\
                   f"{middle_border}\n"\
                   f"HP:  {character['stat_hp']:2d}/{character['stat_max_hp']:3d} "\
                   f"| MP:  {character['stat_mp']:2d}/{character['stat_max_mp']:3d}\n"\
                   f"ATK: {character['stat_atk']:6d} | DEF: {character['stat_def']:6d}\n"\
                   f"MAG: {character['stat_mag']:6d} | MDF: {character['stat_mdf']:6d}\n"\
                   f"SPD: {character['stat_spd']:6d} | LUK: {character['stat_luk']:6d}\n"\
                   f"{border}\n"
        print_character_stats(character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stats_wizard_class_robot_subclass(self, mock_output):
        character = make_character()
        character['class'] = 'Wizard'
        character['subclass'] = 'Robot'
        set_class_bonus(character, 'class')
        set_class_bonus(character, 'subclass')
        stat_length = 14  # Stats are printed as two on each line, 19 characters total
        longest_string = max(len(character['name']), stat_length) + 9
        border = "#" + "=" * longest_string + "#"
        middle_border = "-" * (longest_string + 2)
        expected = f"\n{border}\n" \
                   f"Name:     {character['name']}\n" \
                   f"Class:    {character['class']}\n" \
                   f"Subclass: {character['subclass']}\n" \
                   f"{middle_border}\n" \
                   f"Level: {character['level']:18d}\n" \
                   f"Exp:   {character['exp']:18d}\n" \
                   f"Money: {character['money']:18d}\n" \
                   f"{middle_border}\n" \
                   f"HP:  {character['stat_hp']:2d}/{character['stat_max_hp']:3d} " \
                   f"| MP:  {character['stat_mp']:2d}/{character['stat_max_mp']:3d}\n" \
                   f"ATK: {character['stat_atk']:6d} | DEF: {character['stat_def']:6d}\n" \
                   f"MAG: {character['stat_mag']:6d} | MDF: {character['stat_mdf']:6d}\n" \
                   f"SPD: {character['stat_spd']:6d} | LUK: {character['stat_luk']:6d}\n" \
                   f"{border}\n"
        print_character_stats(character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
