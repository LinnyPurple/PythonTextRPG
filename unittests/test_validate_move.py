from unittest import TestCase
from game import make_board, make_character, validate_move


class TestValidateMove(TestCase):
    def test_validate_move_valid_move(self):
        rows = 25
        columns = 25
        dir_input = 'e'
        board = make_board(rows, columns)
        character = make_character()
        actual = validate_move(board, character, dir_input)
        self.assertTrue(actual)

    def test_validate_move_invalid_move_negative_x(self):
        rows = 25
        columns = 25
        dir_input = 'w'
        board = make_board(rows, columns)
        character = make_character()
        actual = validate_move(board, character, dir_input)
        self.assertFalse(actual)

    def test_validate_move_invalid_move_negative_y(self):
        rows = 25
        columns = 25
        dir_input = 'n'
        board = make_board(rows, columns)
        character = make_character()
        character['x'] = 0
        character['y'] = 0
        actual = validate_move(board, character, dir_input)
        self.assertFalse(actual)

    def test_validate_move_invalid_move_greater_than_rows_columns(self):
        rows = 25
        columns = 25
        dir_input_south = 's'
        dir_input_east = 'e'
        board = make_board(rows, columns)
        character = make_character()
        character['y'] = rows - 1
        actual_south = validate_move(board, character, dir_input_south)
        actual_east = validate_move(board, character, dir_input_east)
        self.assertFalse(actual_south, actual_east)

    def test_validate_move_valid_move_all(self):
        rows = 25
        columns = 25
        dir_input = 'nesw'
        board = make_board(rows, columns)
        character = make_character()
        character['x'] = 18
        character['y'] = 18
        actual = 1
        for coordinate in dir_input:
            actual = actual and validate_move(board, character, coordinate)
        self.assertTrue(actual)

    def test_validate_move_pack(self):
        rows = 25
        columns = 25
        dir_input = 'p'
        board = make_board(rows, columns)
        character = make_character()
        actual = validate_move(board, character, dir_input)
        self.assertTrue(actual)

    def test_validate_move_buy(self):
        rows = 2
        columns = 22
        dir_input = 'b'
        board = make_board(rows, columns)
        character = make_character()
        actual = validate_move(board, character, dir_input)
        self.assertTrue(actual)

    def test_validate_move_inn(self):
        rows = 2
        columns = 22
        dir_input = 'i'
        board = make_board(rows, columns)
        character = make_character()
        actual = validate_move(board, character, dir_input)
        self.assertTrue(actual)
