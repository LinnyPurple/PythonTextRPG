from unittest import TestCase
from game import get_room_status


class TestGetRoomStatus(TestCase):
    def test_get_room_status_init_player(self):
        row = 24
        column = 0
        expected = 'This is the beginning area. No enemies spawn here.'
        actual = get_room_status(row, column)
        self.assertEqual(expected, actual)

    def test_get_room_status_first_area(self):
        row = 22
        column = 16
        expected = 'This is the first area. Made to train for the tough battles ahead.'
        actual = get_room_status(row, column)
        self.assertEqual(expected, actual)

    def test_get_room_status_second_area(self):
        row = 16
        column = 2
        expected = 'This is the second area, void of any color.'
        actual = get_room_status(row, column)
        self.assertEqual(expected, actual)

    def test_get_room_status_third_area(self):
        row = 3
        column = 24
        expected = 'This is the third area, where the mountains are high and temperatures are low.'
        actual = get_room_status(row, column)
        self.assertEqual(expected, actual)

    def test_get_room_status_main_area(self):
        row = 12
        column = 20
        expected = 'This is the main area of the game.'
        actual = get_room_status(row, column)
        self.assertEqual(expected, actual)

    def test_get_room_status_final_area(self):
        row = 0
        column = 0
        expected = 'This is the final area, where the Dream Demon himself lies.'
        actual = get_room_status(row, column)
        self.assertEqual(expected, actual)
