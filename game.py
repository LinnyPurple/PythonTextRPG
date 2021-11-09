"""
Your name: George Rozitis
Your student number: A01253802

All of your code must go in this file.
"""
import random
import time

"""
Questions since Chris took off our "training wheels":
- What would be best defined as constants?
- Can we use classes?
"""


# ~~~ CONSTANTS ~~~
ENCOUNTER_RATE = 20
ATK_MULT = 2
DEF_MULT = 0.5


# ~~~ DATA ~~~
classes = ['fighter', 'warrior', 'cleric', 'wizard', 'thief', 'robot']

enemies = {
    'Dream Cell': {
        'stat_hp': 10,
        'stat_mp': 2,
        'stat_atk': 2,
        'stat_def': 2,
        'stat_mag': 2,
        'stat_mdf': 2,
        'stat_spd': 2,
        'stat_luk': 2,
        'skills': ['Bounce', 'Wait'],
        'exp': 5,
        'money': 2
    },
    'Spider': {
        'stat_hp': 15,
        'stat_mp': 5,
        'stat_atk': 5,
        'stat_def': 1,
        'stat_mag': 3,
        'stat_mdf': 1,
        'stat_spd': 4,
        'stat_luk': 5,
        'skills': ['Bite', 'Crawl'],
        'exp': 8,
        'money': 6
    },
    'Sleep Paralysis Demon': {
        'stat_hp': 1000,
        'stat_mp': 1000,
        'stat_atk': 200,
        'stat_def': 100,
        'stat_mag': 200,
        'stat_mdf': 100,
        'stat_spd': 350,
        'stat_luk': 500,
        'skills': ['Dark Shock'],
        'exp': 10000,
        'money': 10000
    }
}

colors_dict = {
    'b_black': '\033[40m',
    'c_reset': '\033[0m',
    'c_black': '\033[30m',
    'c_red': '\033[91m',
    'c_green': '\033[92m',
    'c_yellow': '\033[93m',
    'c_blue': '\033[94m',
    'c_magenta': '\033[95m',
    'c_cyan': '\033[96m',
    'c_white': '\033[97m'
}


# ~~~ FUNCTIONS ~~~
def get_room_status(row, column):
    """
    Return the room's status on a rectangular game board.

    :param row: An integer representing the given row of the board.
    :param column: An integer representing the given column of the board.
    :precondition: row and column must be positive integers >= 2.
    :postcondition: Determine the room's status as a string for the (row, column)-coordinate on the game board.
    :return: Room status string for the (row, column)-coordinate on the game board.
    """
    return 0


def make_board(rows, columns):
    """
    Return a dictionary made up of (x, y)-coordinates with a string status.

    :param rows: An integer > 1.
    :param columns: An integer > 1.
    :precondition: rows and columns must be integers > 1.
    :postcondition: Creates a dictionary with (x, y)-coordinates as keys and room status as string values.
    :return: A dictionary of rooms' (x, y)-coordinates and their statuses.
    >>> make_board(2, 2)
    {(0, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 0): 'Empty Room', (1, 1): 'Empty Room'}
    >>> make_board(3, 2)
    {(0, 0): 'Empty Room', (0, 1): 'Empty Room', (1, 0): 'Empty Room', (1, 1): 'Empty Room', (2, 0): 'Empty Room', (2, 1): 'Empty Room'}
    """
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = 'Empty Room'
    return board


def make_character():
    """
    Return the player character.

    :return: A dictionary with the player's stats (e.g. name, class, HP, exp, etc.) and (x, y)-coordinates.
    """
    player = {
        'name': '',
        'class': '',
        'subclass': '',
        'level': 1,
        'stat_hp': 5,
        'stat_curr_hp': 5,
        'stat_mp': 5,
        'stat_curr_mp': 5,
        'stat_atk': 2,
        'stat_def': 2,
        'stat_mag': 2,
        'stat_mdf': 2,
        'stat_spd': 2,
        'stat_luk': 2,
        'skills': [],
        'weapon': [],
        'armor': [],
        'exp': 0,
        'money': 0,
        'x': 0,
        'y': 24
    }
    return player


def get_board_rows(board):
    """
    Return the number of rows of the game board.

    :param board: A dictionary of the game board.
    :precondition: board has keys which are tuples of row-column coordinates.
    :precondition: board has values which are coordinate statuses.
    :postcondition: Calculate the number of rows in board.
    :return: Number of rows in board.
    >>> game_board = make_board(4, 4)
    >>> get_board_rows(game_board)
    4
    >>> game_board = make_board(5, 4)
    >>> get_board_rows(game_board)
    5
    """
    return list(board.keys())[-1][0] + 1


def get_board_columns(board):
    """
    Return the number of columns of the game board.

    :param board: A dictionary of the game board.
    :precondition: board has keys which are tuples of row-column coordinates.
    :precondition: board has values which are coordinate statuses.
    :postcondition: Calculate the number of columns in board.
    :return: Number of columns in board.
    >>> game_board = make_board(4, 4)
    >>> get_board_columns(game_board)
    4
    >>> game_board = make_board(4, 5)
    >>> get_board_columns(game_board)
    5
    """
    return list(board.keys())[-1][1] + 1


def invalid_input(wanted_input):
    """
    Print the wanted input to the terminal if given input wasn't valid.

    :param wanted_input: A string representing the wanted input.
    :precondition: wanted_input must be a string.
    :postcondition: Print a string with the wanted input in parentheses divided by forward slashes.
    >>> invalid_input("")
    Invalid input. Please enter one of ().
    >>> invalid_input("yn")
    Invalid input. Please enter one of (y/n).
    >>> invalid_input("1234")
    Invalid input. Please enter one of (1/2/3/4).
    """
    print(f"Invalid input. Please enter one of ({'/'.join(wanted_input)}).")


def set_name():
    """
    Return the user's input for the player's name.

    :return: A string representing the player's name.
    """
    player_name = input("Please enter a name for your character: ")
    while player_name == '' or player_name in ' ' * len(player_name):  # No blank names
        print("A blank name is not accepted.")
        player_name = input("Please enter a name for your character: ")
    # TODO: Use below for one confirmation after setting name/class
    """
    while True:
        confirm_name = input(f"Are you okay with {player_name}? (y/n) ").lower()
        while confirm_name == '' or (confirm_name not in 'yn' and confirm_name not in ['yes', 'no']):
            invalid_input("yn")
            confirm_name = input(f"Are you okay with {player_name}? (y/n) ").lower()
        if confirm_name in 'yes' and len(confirm_name) % 2 != 0:  # Don't accept 'ye'
            break
        elif confirm_name in 'no':
            player_name = input("Please enter a name for your character: ")
            while player_name == '' or player_name in ' ' * len(player_name):  # No blank names
                print("A blank name is not accepted.")
                player_name = input("Please enter a name for your character: ")
    """
    return player_name


def convert_short_class(player_class):
    """
    Return the long form of the class given.

    :param player_class: A string representing the player's class.
    :precondition: player_class must be a string of a valid class ('fighter', 'warrior', 'cleric', 'wizard', 'thief',
                   'robot') of short form (one letter) or long form (the full word).
    :postcondition: Determines the long form of player_class.
    :return: The long form of player_class.
    >>> convert_short_class('f')
    'fighter'
    >>> convert_short_class('cleric')
    'cleric'
    """
    if len(player_class) == 1:
        short_class = 'fkcwtr'
        class_list = ['fighter', 'knight', 'cleric', 'wizard', 'thief', 'robot']
        return class_list[short_class.index(player_class)]
    return player_class


def print_class_descriptions(subclass):
    fighter_text = f"{colors_dict['c_blue']}F{colors_dict['c_reset']}ighter"
    knight_text = f"{colors_dict['c_blue']}K{colors_dict['c_reset']}night"
    cleric_text = f"{colors_dict['c_blue']}C{colors_dict['c_reset']}leric"
    wizard_text = f"{colors_dict['c_blue']}W{colors_dict['c_reset']}izard"
    thief_text = f"{colors_dict['c_blue']}T{colors_dict['c_reset']}hief"
    robot_text = f"{colors_dict['c_blue']}R{colors_dict['c_reset']}obot"
    if subclass:
        print("\nTime to choose the subclass you want to be.")
        print(f"{fighter_text}: +1 HP,  +2 ATK, +1 AGI, +1 LUK")
        print(f"{knight_text}:  +2 HP,  +1 ATK, +2 DEF")
        print(f"{cleric_text}:  +1 HP,  +1 MP,  +1 MAG, +2 MDF")
        print(f"{wizard_text}:  +2 MP,  +2 MAG, +1 MDF")
        print(f"{thief_text}:   +1 ATK, +1 MDF, +2 AGI, +2 LUK")
        print(f"{robot_text}:   +2 HP,  +2 DEF, +1 MDF")
    else:
        print("\nTime to choose the class you want to be.")
        print(f"{fighter_text}: +2 HP,  +3 ATK, +2 AGI, +1 LUK")
        print(f"{knight_text}:  +3 HP,  +2 ATK, +3 DEF")
        print(f"{cleric_text}:  +1 HP,  +2 MP,  +2 MAG, +3 MDF")
        print(f"{wizard_text}:  +3 MP,  +3 MAG, +2 MDF")
        print(f"{thief_text}:   +1 ATK, +1 MDF, +3 AGI, +3 LUK")
        print(f"{robot_text}:   +3 HP,  +3 DEF, +2 MDF")


def set_class(subclass):
    """
    Return the player's class/subclass.

    :param subclass: A boolean representing whether we are setting the player's class or subclass.
    :precondition: subclass must be a boolean with True representing setting the player's subclass and False the
                   player's main class.
    :postcondition: Return the player's class/subclass capitalized.
    :return: The player's class/subclass as a capitalized string.
    """
    print_class_descriptions(subclass)
    player_class = input("What is your selection? ").lower()
    short_class = 'fkcwtr'
    class_list = ['fighter', 'knight', 'cleric', 'wizard', 'thief', 'robot']
    while (player_class not in short_class or (player_class in short_class and len(player_class) != 1))\
            and player_class not in class_list:
        invalid_input(short_class)
        player_class = input("What is your selection? ").lower()
    player_class = convert_short_class(player_class)
    return player_class.title()


def set_class_bonus(character, class_selection):
    """
    Set class/subclass bonuses to character.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param class_selection: A string representing whether we are adding bonuses via the character's class/subclass.
    :precondition: character must be a dictionary with stats.
    :return:
    """
    divider = 1
    if class_selection == 'subclass':
        divider = 2
    if character[class_selection] == 'Fighter':
        character['stat_hp'] += 2 // divider
        character['stat_curr_hp'] += 2 // divider
        character['stat_atk'] += 3 // divider
        character['stat_spd'] += 2 // divider
        character['stat_luk'] += 1
    elif character[class_selection] == 'Knight':
        character['stat_hp'] += 3 // divider
        character['stat_curr_hp'] += 3 // divider
        character['stat_atk'] += 2 // divider
        character['stat_def'] += 3 // divider
    elif character[class_selection] == 'Cleric':
        character['stat_hp'] += 1
        character['stat_curr_hp'] += 1
        character['stat_mp'] += 2 // divider
        character['stat_curr_mp'] += 2 // divider
        character['stat_mag'] += 2 // divider
        character['stat_mdf'] += 3 // divider
    elif character[class_selection] == 'Wizard':
        character['stat_mp'] += 3 // divider
        character['stat_curr_mp'] += 3 // divider
        character['stat_mag'] += 3 // divider
        character['stat_mdf'] += 2 // divider
    elif character[class_selection] == 'Thief':
        character['stat_atk'] += 1
        character['stat_mdf'] += 1
        character['stat_spd'] += 3 // divider
        character['stat_luk'] += 3 // divider
    elif character[class_selection] == 'Robot':
        character['stat_hp'] += 3 // divider
        character['stat_curr_hp'] += 3 // divider
        character['stat_def'] += 3 // divider
        character['stat_mdf'] += 2 // divider


def print_character_stats(character):
    """
    Print the character stats on the screen.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :return:
    """
    stat_length = 14  # Stats are printed as two on each line, 19 characters total
    longest_string = max(len(character['name']), stat_length) + 9
    border = "#" + "=" * longest_string + "#"
    print(f"\n{border}")
    print(f"Name:     {character['name']}")
    print(f"Class:    {character['class']}")
    print(f"Subclass: {character['subclass']}")
    middle_border = "-" * (longest_string + 2)
    print(middle_border)
    print(f"Level: {character['level']:18d}")
    print(f"Money: {character['money']:18d}")
    print(f"HP:  {character['stat_curr_hp']:2d}/{character['stat_hp']:3d} "
          f"| MP:  {character['stat_curr_mp']:2d}/{character['stat_mp']:3d}")
    print(f"ATK: {character['stat_atk']:6d} | DEF: {character['stat_def']:6d}")
    print(f"MAG: {character['stat_mag']:6d} | MDF: {character['stat_mdf']:6d}")
    print(f"SPD: {character['stat_spd']:6d} | LUK: {character['stat_luk']:6d}")
    print(border)


def print_room(row, column, character):
    """
    Print the room given the row and column.

    #=========================#
    |F44O444444444444444444444|
    |========================.|
    |.........................|
    |...........#============T|
    |...........|3333333333333|
    |...........|3333333333333|
    |...........|3333333333333|
    |...........|OOOOO33333333|
    |...........|3333O33333333|
    |...........|B333O33333333|
    |T======#...#=============|
    |2222222|.................|
    |2222222|.................|
    |2222222|.................|
    |2222222|.................|
    |2222222|.................|
    |OOOOOOO|.................|
    |2222222|.................|
    |2222222|.................|
    |222222B|.................|
    |========================B|
    |00001111111111O1111111111|
    |00T01111111111O1111111111|
    |00001111111111O1111111111|
    |00001111111111O1111111111|
    #=========================#

    ---Legend---
    . - Main Area
    0 - Starting Area
    1 - Dungeon 1 (Underground Area)
    2 - Dungeon 2 (Colorless Dungeon)
    3 - Dungeon 3 (Mountain)
    4 - Dungeon 4 (The Dark World)

    B - Boss
    F - Final Boss
    O - Organ Man Event
    T - Town (Buy, Inn)

    :param row: An integer representing the row value on the game board.
    :param column: An integer representing the column value on the game board.
    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: row and column must be integers that are valid row and column values in the game board.
    :precondition: character must be a dictionary with stats and coordinates.
    :return: A string representing the room at (row, column).
    """
    global colors_dict

    if character['x'] == column and character['y'] == row:
        return f"{colors_dict['c_blue']}<P>{colors_dict['c_reset']}"
    # Setting the borders
    elif (row, column) == (-1, -1):
        return "╔"
    elif (row, column) == (-1, 25):
        return "╗"
    elif (row, column) == (25, -1):
        return "╚"
    elif (row, column) == (25, 25):
        return "╝"
    elif (row not in [1, 10, 20] and column in [-1, 25]) or (row, column) == (1, 25) or (row, column) == (10, -1)\
            or (row, column) == (20, 25):
        return "║"
    elif row in [1, 20] and column == -1:
        return "╠"
    elif (row, column) == (20, 7):
        return "═╩═"
    elif (row, column) == (10, 25):
        return "╣"
    elif ((row == 1 or row == 20) and column < 24) or (row == 3 and 12 <= column <= 23)\
            or (row == 10 and (1 <= column <= 6 or 12 <= column <= 24)) or row in [-1, 25]:
        return "═══"
    elif (4 <= row <= 9 and column == 11) or (11 <= row <= 19 and column == 7):
        return " ║ "
    elif (row, column) == (3, 11):
        return " ╔═"
    elif (row, column) == (10, 7):
        return "═╗ "
    elif (row, column) == (10, 11):
        return " ╚═"
    # Setting the colors
    elif 21 <= row <= 24 and column < 4:
        return f"{colors_dict['c_white']}¤¤¤{colors_dict['c_reset']}"
    elif (21 <= row <= 24 and 4 <= column <= 24) or (row, column) == (20, 24):
        return f"{colors_dict['c_magenta']}≡≡≡{colors_dict['c_reset']}"
    elif 10 <= row <= 19 and column <= 7:
        return f"{colors_dict['c_yellow']}◊ð≈{colors_dict['c_reset']}"
    elif 3 <= row <= 9 and 12 <= column <= 24:
        return f"{colors_dict['c_cyan']}△Λ▴{colors_dict['c_reset']}"
    elif (row, column) == (1, 24) or 2 <= row <= 19:
        return f"{colors_dict['c_green']}Îî↑{colors_dict['c_reset']}"
    elif row == 0:
        return f"{colors_dict['b_black']}{colors_dict['c_red']}Ξ♰Ψ{colors_dict['c_reset']}"
    return "   "


def print_board(board, character, square_size):
    """
    Print the board to the terminal.

    :param board: A dictionary of the game board.
    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param square_size: A positive integer representing the width/height of the printed board.
    :precondition: board has keys which are tuples of row-column coordinates.
    :precondition: board has values which are coordinate statuses.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: square_size must be an odd positive integer (to center the player).
    :postcondition: Print current board.
    """
    rows = get_board_rows(board)
    columns = get_board_columns(board)
    square_radius = square_size // 2
    x_left = max(-1, character['x'] - square_radius)
    x_right = min(columns, character['x'] + square_radius)
    y_top = max(-1, character['y'] - square_radius)
    y_bottom = min(rows, character['y'] + square_radius)
    for row in range(y_top, y_bottom + 1):
        printed_row = ""
        for column in range(x_left, x_right + 1):
            printed_row += print_room(row, column, character)
        print(printed_row)


def convert_direction_choice(dir_input):
    """
    Returns the direction input as coordinates.

    :param dir_input: The input given for the direction.
    :precondition: dir_input is a string and a valid directional input (i.e. in '1234nesw', 'north', 'east', 'south',
                   or 'west').
    :postcondition: Determines the (x, y)-coordinates depending on dir_input as a tuple.
    :return: Tuple (x, y)-coordinates depending on dir_input.
    >>> convert_direction_choice('1')
    (0, -1)
    >>> convert_direction_choice('e')
    (1, 0)
    >>> convert_direction_choice('south')
    (0, 1)
    >>> convert_direction_choice('4')
    (-1, 0)
    """
    dir_movement = [0, 0]
    if dir_input in '1n' or dir_input == 'north':
        dir_movement[1] -= 1
    elif dir_input in '2e' or dir_input == 'east':
        dir_movement[0] += 1
    elif dir_input in '3s' or dir_input == 'south':
        dir_movement[1] += 1
    elif dir_input in '4w' or dir_input == 'west':
        dir_movement[0] -= 1
    return tuple(dir_movement)


def get_user_choice():
    """
    Return the user's coordinate choice.

    :return: Tuple (x, y)-coordinates depending on user's input.
    """
    print("1. (N)orth\n2. (E)ast\n3. (S)outh\n4. (W)est")
    dir_input = input("Which direction do you want to go? ").lower()
    short_list = '1234nesw'
    coordinate_list = ['north', 'east', 'south', 'west']
    while (dir_input not in short_list or (dir_input in short_list and len(dir_input) != 1))\
            and dir_input not in coordinate_list:
        print("Invalid input.")
        dir_input = input("Which direction do you want to go? ").lower()
    return dir_input


def is_wall(row, column, character):
    wall_strings = ["╔", "╗", "╚", "╝", "║", "╩", "═"]
    for wall_string in wall_strings:
        if wall_string in print_room(row, column, character):
            return True
    return False


def validate_move(board, character, direction):
    """
    Return whether a player's directional input is possible.

    :param board: A dictionary of the game board.
    :param character: A dictionary of the player.
    :param direction: A string which is the given direction.
    :precondition: board has keys which are tuples of row-column coordinates.
    :precondition: board has values which are coordinate statuses.
    :precondition: character has keys/values with board coordinates and current HP.
    :precondition: direction is a string and a valid directional input (i.e. in '1234nesw', 'north', 'east', 'south',
                   or 'west').
    :postcondition: Return whether direction on board is valid for character.
    :return: Whether direction on board is valid for character.
    >>> game_board = make_board(4, 4)
    >>> player = make_character()
    >>> move_east = convert_direction_choice('e')
    >>> validate_move(game_board, player, move_east)
    True
    >>> move_west = convert_direction_choice('w')
    >>> validate_move(game_board, player, move_west)
    False
    """
    rows = get_board_rows(board)
    columns = get_board_columns(board)
    direction_tuple = convert_direction_choice(direction)
    new_x = character['x'] + direction_tuple[0]
    new_y = character['y'] + direction_tuple[1]
    inbound = 0 <= new_x < columns and 0 <= new_y < rows
    wall = is_wall(new_y, new_x, character)
    return inbound and not wall


def move_character(character, direction):
    """
    Update the character's (x, y)-coordinates.

    :param character: A dictionary of the player.
    :param direction: A string which is the given direction.
    :precondition: character has keys/values with board coordinates and current HP.
    :precondition: direction is a string and a valid directional input (i.e. in '1234nesw', 'north', 'east', 'south',
                   or 'west').
    :postcondition: Update character's (x, y)-coordinates via direction.
    """
    direction_tuple = convert_direction_choice(direction)
    character['x'] += direction_tuple[0]
    character['y'] += direction_tuple[1]


def game():
    """
    Runs through the game's logic.
    """
    # ~~~ Set variables ~~~
    rows = 25
    columns = 25
    board = make_board(rows, columns)
    character = make_character()
    selecting_subclass = False
    # INTRO FUNCTION
    character['name'] = set_name()
    character['class'] = set_class(selecting_subclass)
    set_class_bonus(character, 'class')
    selecting_subclass = True
    character['subclass'] = set_class(selecting_subclass)
    if character['subclass'] == character['class']:
        print("\nThat's already your main class. Please choose again.")
        character['subclass'] = set_class(selecting_subclass)
    set_class_bonus(character, 'subclass')
    print_character_stats(character)
    valid_move = False  # Added here so I don't output the map twice.
    while True:
        if not valid_move:  # Added here so I don't output the map twice.
            print_board(board, character, 7)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            print_board(board, character, 7)
        else:
            print("Can't move here.")


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
