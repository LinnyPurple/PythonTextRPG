from unittest import TestCase
from game import make_board, get_board_columns


class TestGetBoardColumns(TestCase):
    def test_get_board_columns_rows_same(self):
        rows = 5
        columns = 5
        board = make_board(rows, columns)
        expected = 5
        actual = get_board_columns(board)
        self.assertEqual(expected, actual)

    def test_get_board_columns_rows_different(self):
        rows = 5
        columns = 4
        board = make_board(rows, columns)
        expected = 4
        actual = get_board_columns(board)
        self.assertEqual(expected, actual)
