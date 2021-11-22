from unittest import TestCase
from unittest.mock import patch
from game import get_color, print_class_descriptions
import io


class TestPrintClassDescriptions(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_descriptions_class(self, mock_output):
        subclass = False
        fighter_text = f"1. ({get_color('c_blue')}F{get_color('c_reset')})ighter"
        knight_text = f"2. ({get_color('c_blue')}K{get_color('c_reset')})night"
        cleric_text = f"3. ({get_color('c_blue')}C{get_color('c_reset')})leric"
        wizard_text = f"4. ({get_color('c_blue')}W{get_color('c_reset')})izard"
        thief_text = f"5. ({get_color('c_blue')}T{get_color('c_reset')})hief"
        robot_text = f"6. ({get_color('c_blue')}R{get_color('c_reset')})obot"
        expected = f"\nTime to choose the class you want to be.\n"\
                   f"{fighter_text}: +2 HP,  +3 ATK, +2 SPD, +1 LUK\n"\
                   f"\t- A strong class with high attack and speed. Anything the crosses your fists will meet their " \
                   f"maker.\n"\
                   f"{knight_text}:  +3 HP,  +2 ATK, +3 DEF\n"\
                   f"\t- A heroic class with high health and defense. Regular enemies will have a hard time hurting " \
                   f"you.\n"\
                   f"{cleric_text}:  +1 HP,  +2 MP,  +2 MAG, +3 MDF\n"\
                   f"\t- A supportive class with a healing spell. You can keep some money by not spending lots on " \
                   f"potions.\n"\
                   f"{wizard_text}:  +3 MP,  +3 MAG, +2 MDF\n"\
                   f"\t- A firey class with a fire spell. The enemies facing you will for sure be burned.\n"\
                   f"{thief_text}:   +1 ATK, +1 MDF, +3 SPD, +3 LUK\n"\
                   f"\t- A hasty class with high speed and luck. Your skill can increase your critical hit chance.\n"\
                   f"{robot_text}:   +3 HP,  +3 DEF, +2 MDF\n"\
                   f"\t- A metallic class that gets bonuses in defense. You can even analyze the enemy's stats.\n"
        print_class_descriptions(subclass)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_descriptions_subclass(self, mock_output):
        subclass = True
        fighter_text = f"1. ({get_color('c_blue')}F{get_color('c_reset')})ighter"
        knight_text = f"2. ({get_color('c_blue')}K{get_color('c_reset')})night"
        cleric_text = f"3. ({get_color('c_blue')}C{get_color('c_reset')})leric"
        wizard_text = f"4. ({get_color('c_blue')}W{get_color('c_reset')})izard"
        thief_text = f"5. ({get_color('c_blue')}T{get_color('c_reset')})hief"
        robot_text = f"6. ({get_color('c_blue')}R{get_color('c_reset')})obot"
        expected = f"\nTime to choose the subclass you want to be.\n"\
                   f"{fighter_text}: +1 HP,  +2 ATK, +1 SPD, +1 LUK\n"\
                   f"{knight_text}:  +2 HP,  +1 ATK, +2 DEF\n"\
                   f"{cleric_text}:  +1 HP,  +1 MP,  +1 MAG, +2 MDF\n"\
                   f"{wizard_text}:  +2 MP,  +2 MAG, +1 MDF\n"\
                   f"{thief_text}:   +1 ATK, +1 MDF, +2 SPD, +2 LUK\n"\
                   f"{robot_text}:   +2 HP,  +2 DEF, +1 MDF\n"
        print_class_descriptions(subclass)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
