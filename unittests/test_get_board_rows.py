from unittest import TestCase
from game import make_board, get_board_rows


class TestGetBoardRows(TestCase):
    def test_get_board_rows_columns_same(self):
        rows = 5
        columns = 5
        board = make_board(rows, columns)
        expected = 5
        actual = get_board_rows(board)
        self.assertEqual(expected, actual)

    def test_get_board_rows_columns_different(self):
        rows = 4
        columns = 5
        board = make_board(rows, columns)
        expected = 4
        actual = get_board_rows(board)
        self.assertEqual(expected, actual)
