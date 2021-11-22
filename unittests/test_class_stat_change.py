from unittest import TestCase
from unittest.mock import patch
from game import make_character, class_stat_change


class TestClassStatChange(TestCase):
    @patch('random.randint', return_value=5)
    def test_class_stat_change_class_robot_hp(self, random_number_generator):
        character = make_character()
        class_type = 'class'
        character[class_type] = 'Robot'
        expected = 5
        actual = class_stat_change('hp', character, class_type)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_class_stat_change_class_wizard_hp(self, random_number_generator):
        character = make_character()
        class_type = 'class'
        character[class_type] = 'Wizard'
        expected = 0
        actual = class_stat_change('hp', character, class_type)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_class_stat_change_subclass_knight_hp(self, random_number_generator):
        character = make_character()
        class_type = 'subclass'
        character[class_type] = 'Knight'
        expected = 2
        actual = class_stat_change('hp', character, class_type)
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_class_stat_change_subclass_wizard_hp(self, random_number_generator):
        character = make_character()
        class_type = 'subclass'
        character[class_type] = 'Wizard'
        expected = 0
        actual = class_stat_change('hp', character, class_type)
        self.assertEqual(expected, actual)
