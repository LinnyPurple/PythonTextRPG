from unittest import TestCase
from game import get_room_status, make_board


class TestMakeBoard(TestCase):
    def test_make_board_rows_columns_same_size(self):
        rows = 2
        columns = 2
        expected = {(0, 0): 'This is the final area, where the Dream Demon himself lies.',
                    (0, 1): 'This is the final area, where the Dream Demon himself lies.', (1, 0): None, (1, 1): None}
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_board_rows_columns_different_size(self):
        rows = 3
        columns = 2
        expected = {(0, 0): 'This is the final area, where the Dream Demon himself lies.',
                    (0, 1): 'This is the final area, where the Dream Demon himself lies.', (1, 0): None, (1, 1): None,
                    (2, 0): 'This is the main area of the game.', (2, 1): 'This is the main area of the game.'}
        actual = make_board(rows, columns)
        self.assertEqual(expected, actual)
