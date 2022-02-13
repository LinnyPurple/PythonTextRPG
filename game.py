"""
Your name: George Rozitis

All of your code must go in this file.
"""
import itertools
import math
import random
import sys
import vlc

"""
Find all functions by the following regex: def ([a-z]|\_)*(\({1}([a-z]|\_|\,|\s)*\){1}):{1}
"""


# ~~~ FUNCTIONS ~~~
def get_color(color: str) -> str:
    """
    Return a string to change the color on the screen.

    :param color: A string representing the color.
    :precondition: color must be a key string in local variable colors_dict.
    :postcondition: Return the string value from key color.
    :return: A string.
    """
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
    return colors_dict[color]


def get_room_status(row: int, column: int) -> str:
    """
    Return the room's status on a rectangular game board.

    :param row: An integer representing the given row of the board.
    :param column: An integer representing the given column of the board.
    :precondition: row and column must be positive integers >= 2.
    :postcondition: Determine the room's status as a string for the (row, column)-coordinate on the game board.
    :return: Room status string for the (row, column)-coordinate on the game board.
    >>> get_room_status(24, 0)
    'This is the beginning area. No enemies spawn here.'
    >>> get_room_status(22, 16)
    'This is the first area. Made to train for the tough battles ahead.'
    >>> get_room_status(0, 0)
    'This is the final area, where the Dream Demon himself lies.'
    """
    if 21 <= row <= 24 and column < 4:
        return f"This is the beginning area. No enemies spawn here."
    elif (21 <= row <= 24 and 4 <= column <= 24) or (row, column) == (20, 24):
        return f"This is the first area. Made to train for the tough battles ahead."
    elif 10 <= row <= 19 and column <= 7:
        return f"This is the second area, void of any color."
    elif 3 <= row <= 9 and 12 <= column <= 24:
        return f"This is the third area, where the mountains are high and temperatures are low."
    elif (row, column) == (1, 24) or 2 <= row <= 19:
        return f"This is the main area of the game."
    elif row == 0:
        return f"This is the final area, where the Dream Demon himself lies."


def make_board(rows: int, columns: int) -> dict:
    """
    Return a dictionary made up of (x, y)-coordinates with a string status.

    :param rows: An integer > 1.
    :param columns: An integer > 1.
    :precondition: rows and columns must be integers > 1.
    :postcondition: Creates a dictionary with (x, y)-coordinates as keys and room status as string values.
    :return: A dictionary of rooms' (x, y)-coordinates and their statuses.
    >>> make_board(2, 2)
    {(0, 0): 'This is the final area, where the Dream Demon himself lies.', \
(0, 1): 'This is the final area, where the Dream Demon himself lies.', (1, 0): None, (1, 1): None}
    """
    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = get_room_status(row, column)
    return board


def make_character() -> dict:
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
        'stat_max_hp': 5,
        'stat_mp': 5,
        'stat_max_mp': 5,
        'stat_atk': 2,
        'stat_def': 2,
        'stat_mag': 2,
        'stat_mdf': 2,
        'stat_spd': 2,
        'stat_luk': 2,
        'skills': [],
        'items': {},
        'exp': 0,
        'money': 0,
        'x': 0,
        'y': 24
    }
    return player


def get_board_rows(board: dict) -> int:
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


def get_board_columns(board: dict) -> int:
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


def invalid_input(wanted_input: str) -> None:
    """
    Print the wanted input to the terminal if given input wasn't valid.

    :param wanted_input: A string representing the wanted input.
    :precondition: wanted_input must be a string.
    :postcondition: Print a string with the wanted input in parentheses divided by forward slashes.
    >>> invalid_input("")
    Invalid input. Please enter one of ().
    >>> invalid_input("  yn")
    Invalid input. Please enter one of (y/n).
    >>> invalid_input("    1234")
    Invalid input. Please enter one of (1/2/3/4).
    """
    print(f"Invalid input. Please enter one of ({'/'.join(wanted_input[len(wanted_input) // 2:])}).")


def set_name() -> str:
    """
    Return the user's input for the player's name.

    :return: A string representing the player's name.
    """
    player_name = input("Please enter a name for your character: ")
    while player_name == '' or player_name in ' ' * len(player_name):  # No blank names
        print(f"A blank name is not accepted.")
        player_name = input("Please enter a name for your character: ")
    return player_name


def convert_short_input(player_input: str, short_input: str, long_input: list) -> str:
    """
    Return the long form of the class given.

    :param player_input: A string representing the player's class.
    :param short_input: A string represting the list of one-character possible inputs.
    :param long_input: A list of strings representing the list of one-word inputs.
    :precondition: player_input must be a string of a valid input in short_input or long_input.
    :precondition: short_input must be a string with one-character possible inputs in 'number-then-letter' order.
    :precondition: long_input must be a list of strings with each element being a possible input.
    :postcondition: Determines the long form of player_input.
    :return: A string representing the long form of player_input.
    >>> short_class = '123456fkcwtr'
    >>> class_list = ['fighter', 'knight', 'cleric', 'wizard', 'thief', 'robot']
    >>> convert_short_input('f', short_class, class_list)
    'fighter'
    >>> convert_short_input('2', short_class, class_list)
    'knight'
    >>> convert_short_input('cleric', short_class, class_list)
    'cleric'
    >>> short_battle_input = '1234asif'
    >>> battle_input_list = ['attack', 'skill', 'item', 'flee']
    >>> convert_short_input('s', short_battle_input, battle_input_list)
    'skill'
    >>> convert_short_input('flee', short_battle_input, battle_input_list)
    'flee'
    """
    if len(player_input) == 1 and ord('1') <= ord(player_input) <= ord('9'):
        return long_input[int(player_input) - 1]
    elif len(player_input) == 1:
        return long_input[short_input.index(player_input) - len(long_input)]
    return player_input


def print_class_descriptions(subclass: bool) -> None:
    fighter_text = f"1. ({get_color('c_blue')}F{get_color('c_reset')})ighter"
    knight_text = f"2. ({get_color('c_blue')}K{get_color('c_reset')})night"
    cleric_text = f"3. ({get_color('c_blue')}C{get_color('c_reset')})leric"
    wizard_text = f"4. ({get_color('c_blue')}W{get_color('c_reset')})izard"
    thief_text = f"5. ({get_color('c_blue')}T{get_color('c_reset')})hief"
    robot_text = f"6. ({get_color('c_blue')}R{get_color('c_reset')})obot"
    if subclass:
        print(f"\nTime to choose the subclass you want to be.\n"
              f"{fighter_text}: +1 HP,  +2 ATK, +1 SPD, +1 LUK\n"
              f"{knight_text}:  +2 HP,  +1 ATK, +2 DEF\n"
              f"{cleric_text}:  +1 HP,  +1 MP,  +1 MAG, +2 MDF\n"
              f"{wizard_text}:  +2 MP,  +2 MAG, +1 MDF\n"
              f"{thief_text}:   +1 ATK, +1 MDF, +2 SPD, +2 LUK\n"
              f"{robot_text}:   +2 HP,  +2 DEF, +1 MDF")
    else:
        print(f"\nTime to choose the class you want to be.\n"
              f"{fighter_text}: +2 HP,  +3 ATK, +2 SPD, +1 LUK\n"
              f"\t- A strong class with high attack and speed. Anything the crosses your fists will meet their maker.\n"
              f"{knight_text}:  +3 HP,  +2 ATK, +3 DEF\n"
              f"\t- A heroic class with high health and defense. Regular enemies will have a hard time hurting you.\n"
              f"{cleric_text}:  +1 HP,  +2 MP,  +2 MAG, +3 MDF\n"
              f"\t- A supportive class with a healing spell. You can keep some money by not spending lots on potions.\n"
              f"{wizard_text}:  +3 MP,  +3 MAG, +2 MDF\n"
              f"\t- A firey class with a fire spell. The enemies facing you will for sure be burned.\n"
              f"{thief_text}:   +1 ATK, +1 MDF, +3 SPD, +3 LUK\n"
              f"\t- A hasty class with high speed and luck. Your skill can increase your critical hit chance.\n"
              f"{robot_text}:   +3 HP,  +3 DEF, +2 MDF\n"
              f"\t- A metallic class that gets bonuses in defense. You can even analyze the enemy's stats.")


def set_class(subclass: bool) -> str:
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
    short_class = '123456fkcwtr'
    class_list = ['fighter', 'knight', 'cleric', 'wizard', 'thief', 'robot']
    while (player_class not in short_class or (player_class in short_class and len(player_class) != 1))\
            and player_class not in class_list:
        invalid_input(short_class)
        player_class = input("What is your selection? ").lower()
    player_class = convert_short_input(player_class, short_class, class_list)
    return player_class.title()


def set_class_bonus(character: dict, class_selection: str) -> None:
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
    class_bonuses = {
        'Fighter': {
            'hp': 2,
            'atk': 3,
            'spd': 2,
            'luk': 1
        },
        'Knight': {
            'hp': 3,
            'atk': 2,
            'def': 3
        },
        'Cleric': {
            'hp': 1,
            'mp': 2,
            'mag': 2,
            'mdf': 3
        },
        'Wizard': {
            'mp': 3,
            'mag': 3,
            'mdf': 2
        },
        'Thief': {
            'atk': 1,
            'mdf': 1,
            'spd': 3,
            'luk': 3
        },
        'Robot': {
            'hp': 3,
            'def': 3,
            'mdf': 2
        }
    }
    class_dict = class_bonuses[character[class_selection]]
    for stat_bonus in class_dict:
        character['stat_' + stat_bonus] += math.ceil(class_dict[stat_bonus] / divider)
        if stat_bonus in 'hpmp':
            character['stat_max_' + stat_bonus] += math.ceil(class_dict[stat_bonus] / divider)


def intro() -> None:
    """
    Print the intro sequence of the game.
    """
    print(f"- You find yourself waking up in a quiet area that you can't seem to recognize. Slowly picking yourself\n"
          f"  off the ground, the surrounding area is a clear, white abyss. Almost nothing to the eye.\n"
          f"- From your left, someone walks by and stops beside you. He has a large straw hat on, but you can't see\n"
          f"  his eyes. Turning over to you, he begins to speak.\n"
          f"???: He got you too, didn't he?\n"
          f"- But you don't know what he's talking about. 'He got you too'? What happened when you fell asleep?\n"
          f"???: I've been trying to find a cure to wake myself up, but I heard the only way to get it is by kiiling\n"
          f"     the Dream Demon. But nobody's been strong enough to face off against him. They all become obstacles\n"
          f"     for the rest of us who fight to open our eyes once again.\n"
          f"- Without a word, he walks off, leaving you there to ponder over what happened. You try to remember bits\n"
          f"  and pieces about yourself, but only come up with your name.\n"
          f"- So...who are you, anyways?")


def switch_statements() -> dict:
    """
    Set the switch statements.

    :return: A dictionary with keys listing events and boolean values if they happened (initially set to False).
    """
    events = {
        'organ_man_1': False,
        'organ_man_2': False,
        'organ_man_final': False,
        'first_town_first_visit': False,
        'colorless_first_visit': False,
        'mountains_first_visit': False,
        'boss_1': False,
        'boss_2': False,
        'boss_3': False,
        'boss_final': False
    }
    return events


def check_town_events(character: dict, events: dict) -> None:
    """
    Run through a town event.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param events: A dictionary with event string keys and boolean values (if they happened).
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: events must be a dictionary with string keys and boolean values (True if happened, False otherwise).
    :postcondition: Check if event needs to occur depending on character's location.
    """
    if (character['x'], character['y']) == (2, 22) and not events['first_town_first_visit']:
        print(f"- Welcome to the first town of the game!\n"
              f"- Here, you can buy items and sleep at the inn.\n")
        events['first_town_first_visit'] = True
    elif (character['x'], character['y']) == (0, 10) and not events['colorless_first_visit']:
        print(f"- As you enter this new town, you notice instantly how...colorless the town is. White and black as\n"
              f"  far as the eye can see. You take a look at yourself...you still have the color on your body. So\n"
              f"  what happened?\n"
              f"- You see someone come up to you, someone void of color. He looks sad.\n"
              f"???: Hey. You an outsider?\n"
              f"- You nod hesitantly. His voice is sharp like a large blade.\n"
              f"J: The name's J. I built this town with my bare hands, but overnight, the color just...poof! Gone!\n"
              f"   Ya look like someone who could help bring it back. Could ya do it for me?\n"
              f"- He casually cracks his fingers, making you nod in response.\n"
              f"J: I'm certain there's something to bring the color back around here somewhere...a dark, sinister\n"
              f"   creature came by here once, making the rest of the townsfolk cower in fear. I'll give ya a nice\n"
              f"   reward if ya can bring my town back to life!")
        events['colorless_first_visit'] = True
    elif (character['x'], character['y']) == (24, 3) and not events['mountains_first_visit']:
        print(f"- The grassy terrain changes into one of thick, white snow. Your feet sink into the snow, leaving a\n"
              f"  noticeable footprint with each step you take. Colorful lights are strung along the walls of every\n"
              f"  house, each one a quaint little wooden cabin. You feel like you could live here for a long time.\n"
              f"- Suddenly, you see something gracefully walk across the snow: a bipedal panda, only six inches tall.\n"
              f"  It's wearing a pink, blue and white cloth around its body, and stops right by your feet.\n"
              f"Panda: OH MY GOSH!\n"
              f"- Staring up at you, the panda climbs up your leg and up your torso. Trying to remove it from your\n"
              f"  body doesn't do anything, allowing it to climb up to your face. Once there, it positions itself\n"
              f"  and begins to boop you on the nose with immense speed. Even though the panda is blocking your view,\n"
              f"  it feels quite nice to have a soft, fluffy panda comforting you in such a way.\n"
              f"???: Ahem!\n"
              f"- A loud cough comes from in front of you, and the panda stops booping. It turns around and jumps off\n"
              f"  you in shock.\n"
              f"Panda: MAMA!\n"
              f"???: Ali, what did we say about booping strangers?\n"
              f"Ali: But mama...they looked very cold!\n"
              f"???: I know, I know.\n"
              f"- The black-haired woman takes the panda and lets it rest on her shoulder.\n"
              f"Katt: I'm sorry...{character['name']}, thanks. I'm Katt, the mayor of this town. Ali here is a\n"
              f"      little...what should I say? ...Fiesty.\n"
              f"Ali: I am NOT, mama!\n"
              f"- Katt chuckles at Ali's reaction.\n"
              f"Katt: Though she has been a little more...upset, so to speak.\n"
              f"Ali: Yeah! Greystone's nose has disappeared!\n"
              f"Katt: Greystone's one of her best friends. A much smaller panda. He woke up one day without his\n"
              f"      nose, and his fur has slowly been coming off.\n"
              f"Ali: Can you please help find it? I don't want his fur to go away!\n"
              f"- Ali cowers her head. You feel guilty and accept their request.\n"
              f"Katt: A group of theives have been stealing things and head off to the farthest mountains. I'm\n"
              f"      certain they've went there. We wish you the best of luck!")
        events['mountains_first_visit'] = True


def check_organ_man_events(character: dict, events: dict) -> None:
    """
    Run through an Organ Man event.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param events: A dictionary with event string keys and boolean values (if they happened).
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: events must be a dictionary with string keys and boolean values (True if happened, False otherwise).
    :postcondition: Check if event needs to occur depending on character's location.
    """
    if character['x'] == 14 and character['y'] >= 21 and not events['organ_man_1']:
        print(f"???: HOLY CRAP, IS THAT ORGAN MAN!?\n"
              f"- You hear someone shouting that isn't you. A well-suited man rolls over in a portable organ. He looks"
              f"  very cheery.\n"
              f"Organ Man: WELL, WELL, WELL...WHAT DO WE HAVE HERE? IT IS I, ORGAN MAN, WHO LIVES WITH MY TRUSTY\n"
              f"ORGAN! DO YOU CARE TO DUEL ME IN A BATTLE OF MUSIC?")
        battle(character, get_enemy('Organ Man'))
        print(f"Organ Man: WOW, YOU ARE VERY STRONG! 'TILL WE MEET AGAIN!\n"
              f"- Organ Man rolls away, the sounds of his organ disappearing along with him.")
        events['organ_man_1'] = True
    elif ((character['x'] < 7 and character['y'] == 16) or (12 <= character['x'] <= 16 and character['y'] == 7)
            or (character['x'] == 16 and character['y'] in [8, 9])) and not events['organ_man_2']:
        print(f"???: HOLY CRAP, IS THAT ORGAN MAN!?\n"
              f"- The familiar sounds of the organ come your way. Despite the music sounding nice, Organ Man looks\n"
              f"  tattered.\n"
              f"Organ Man: WELL, WELL, WELL...WE MEET AGAIN, {character['name'].upper()}! NEVER EXPECTED TO SEE YOU\n"
              f"           HERE! WELL THEN...SHALL WE ORCHESTRATE ANOTHER DUEL OF EPIC PROPORTIONS!?")
        battle(character, get_enemy('Organ Man'))
        print(f"Organ Man: BESTED ONCE AGAIN! YOU CONTINUE TO PROVE ME WRONG! 'TILL WE MEET AGAIN!\n"
              f"- You watch as Organ Man plays the piano as he fades into the distance.")
        events['organ_man_2'] = True
    elif character['x'] == 3 and character['y'] == 0 and not events['organ_man_final']:
        print(f"???: HOLY CRAP, IS THAT ORGAN MAN!?\n"
              f"- You were only steps away from the Dream Demon's room until you heard his voice...again.\n"
              f"Organ Man: WELL, WELL, WELL...IF IT ISN'T {character['name'].upper()}! IT HAS BEEN FUN WATCHING YOU\n"
              f"           PRANCE AROUND THIS QUAINT LITTLE WORLD, BUT IT SEEMS WE CROSS PATHS ONCE MORE! ARE YOU\n"
              f"           READY FOR THE GREATEST FIGHT OF YOUR LIFE!?")
        battle(character, get_enemy('Organ Man'))
        print(f"- It was a tough battle, but Organ Man looks tired. Completely beat, his hands droop from the piano.\n"
              f"Organ Man: HA...HAAA...HAAAaa...I've been bested...once again...by you.\n"
              f"- He somberly turns to you.\n"
              f"Organ Man: You sure you want to take on the Dream Demon?\n"
              f"- You nod.\n"
              f"Organ Man: So be it...I can't stop you, can I? Maybe I just had too much fun here. Maybe it's my time\n"
              f"           to wake up from this dream too...")
        events['organ_man_final'] = True


def check_boss_events(character: dict, events: dict) -> None:
    """
    Run through a boss event.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param events: A dictionary with event string keys and boolean values (if they happened).
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: events must be a dictionary with string keys and boolean values (True if happened, False otherwise).
    :postcondition: Check if event needs to occur depending on character's location.
    """
    if (character['x'], character['y']) == (24, 20) and not events['boss_1']:
        print(f"- A large, menacing humanoid figure made of straw blocks the way. It has a matching straw hat and\n"
              f"isn't budging a bit. It stares down at you as if it has seen you before...\n"
              f"...but it suddenly grabs out towards you! It doesn't look like this fiend won't go down without a\n"
              f"fight!")
        battle(character, get_enemy('Straw Beast'))
        print(f"The surrounding area is filled with pieces of straw. Your eyes swell up, but you can't explain why.\n"
              f"Though the path is now clear, allowing you to venture further into this world!")
        events['boss_1'] = True
        vlc.MediaPlayer(r'\music\success.wav').play()
    elif (character['x'], character['y']) == (6, 19) and not events['boss_2']:
        print(f"- As you walk around, you notice a small black dot making its way towards you. Turning around, you\n"
              f"  find yourself lost. You might not be able to find your way back.\n"
              f"- Focusing back on the black dot, which is now at least twice your height, it rushes towards you,\n"
              f"  instigating a fight!")
        battle(character, get_enemy('Void'))
        print(f"- With one last attack, you remove the void from the world. It emits a large explosion of color,\n"
              f"  bringing back life to the area that was once lost.\n"
              f"???: I thought ya could do it.\n"
              f"- The voice comes from J, who has a smile on his face.\n"
              f"J: Nobody's been strong enough to take on the void, especially all by themselves. Here's the reward\n"
              f"   I promised.\n"
              f"- He gives you 500 money!\n"
              f"J: Come back whenever. I'm glad to have met ya. Ya saved me and my town, and I'll be forever\n"
              f"   grateful.\n"
              f"- He walks off. Getting a chance to look around, it's much easier to make your way back.")
        events['boss_2'] = True
        vlc.MediaPlayer(r'\music\success.wav').play()
    elif (character['x'], character['y']) == (12, 9) and not events['boss_3']:
        print(f"- Walking up some stairs, you find yourself at the peak of the mountain. A bunch of tattered clothes\n"
              f"  are spread across a long walkway, which leads to an empty glass throne. On the seat is a black\n"
              f"  speck. You can't tell what it is until you feel something crawl down your body.\n"
              f"- It's Ali.\n"
              f"Ali: OH MY GOSH! It's Greystone's nose!\n"
              f"- You cough into your arm, getting her attention.\n"
              f"Ali: Ah...sorry. I jumped onto your back. I thought you'd notice. Hahahaha!\n"
              f"- She grabs Greystone's nose and climbs off the chair. The two of you start walking away.\n"
              f"???: You think of leaving with that thing in hand?"
              f"- You both turn around and see a purple-skinned man in a black cloak. He has a crooked, dark red wand\n"
              f"  in his right hand.\n"
              f"???: That object belongs to me.\n"
              f"Ali: It does NOT!\n"
              f"- Ali conjures up a blast of light and attacks the cloaked man, but he fights back with a dark ball,\n"
              f"  sending Ali back a few meters.\n"
              f"Ali: Oh nyooo! {character['name']}, help me!\n"
              f"- You ready your weapon and lurch at the man.")
        battle(character, get_enemy('Dark Lord'))
        print(f"- Defeating the Dark Lord, he slumps down on the cold floor, falling into an eternal sleep.\n"
              f"Ali: OH MY GOSH! You did it!\n"
              f"- Ali jumps onto your face and boops you.\n"
              f"Ali: YAAAAAY!!! Greystone's gonna be fine!\n"
              f"- A set of footsteps reach you, getting Ali's attention. It's Katt.\n"
              f"Ali: MAMA! I have Greystone's nose!\n"
              f"Katt: Oh, thank goodness you're safe!\n"
              f"- She emotinally embraces Ali.\n"
              f"Katt: Greystone said you'd be here, so I brought him with me. Please don't run off like that again.\n"
              f"Ali: But mamaaa...Greystone's nose!\n"
              f"- Ali gives it to Katt.\n"
              f"Katt: Oh! That is his!\n"
              f"- She brings out Greystone, who looks really pale. Placing his nose where it should be brings life\n"
              f"  and color back to his body.\n"
              f"Katt: He's getting better! {character['name']}, I don't know how I can thank you more. Please, take\n"
              f"      some of these specially-made candies. They'll make you stronger.\n")
        if 'Super Candy' not in character['items'].keys():
            character['items']['Super Candy'] = 0
        character['items']['Super Candy'] += 3
        print(f"- You got 3 Super Candy!\n"
              f"Katt: Thank you so much for helping Greystone heal up. He can play with Ali again!\n"
              f"Ali: Yaaay!!!\n"
              f"Katt: Come over and visit if you get the time. I'm sure Ali and Greystone would love to see you\n"
              f"      again.\n"
              f"Ali: Yeah! See you soon, {character['name']}!\n"
              f"- They walk down the mountain as you spend some time admiring the view. You haven't been this high up\n"
              f"  this whole time. You wonder if you'll ever get this experience again.")
        events['boss_3'] = True
        vlc.MediaPlayer(r'\music\success.wav').play()
    elif (character['x'], character['y']) == (0, 0) and not events['boss_final']:
        print(f"- You look up and see a dark, ominous creature standing before you - the Dream Demon itself. It\n"
              f"  brings out its blade and prepares to fight.")
        battle(character, get_enemy('Dream Demon'))
        print(f"- With one more attack, you kill the Dream Demon, bringing the world with a huge glow of light.\n"
              f"  Your eyes are blinded by it, forcing them to close. And the next time you open them, you finally\n"
              f"  wake up in your bed, feeling stronger than ever.")
        events['boss_final'] = True
        vlc.MediaPlayer(r'\music\success.wav').play()


def check_events(character: dict, events: dict) -> None:
    """
    Run an event if there is one where the character is and hasn't been executed.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param events: A dictionary representing events that have happened in the game.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: events must be a dictionary with string keys and boolean values.
    :postcondition: Run the given event if not run yet.
    """
    check_town_events(character, events)
    check_organ_man_events(character, events)
    check_boss_events(character, events)


def print_character_stats(character: dict) -> None:
    """
    Print the character stats on the screen.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Prints out the character's stats in a formatted pattern on the screen.
    """
    stat_length = 14  # Stats are printed as two on each line, 19 characters total
    longest_string = max(len(character['name']), stat_length) + 9
    border = "#" + "=" * longest_string + "#"
    middle_border = "-" * (longest_string + 2)
    print(f"\n{border}\n"
          f"Name:     {character['name']}\n"
          f"Class:    {character['class']}\n"
          f"Subclass: {character['subclass']}\n"
          f"{middle_border}\n"
          f"Level: {character['level']:18d}\n"
          f"Exp:   {character['exp']:18d}\n"
          f"Money: {character['money']:18d}\n"
          f"{middle_border}\n"
          f"HP:  {character['stat_hp']:2d}/{character['stat_max_hp']:3d} "
          f"| MP:  {character['stat_mp']:2d}/{character['stat_max_mp']:3d}\n"
          f"ATK: {character['stat_atk']:6d} | DEF: {character['stat_def']:6d}\n"
          f"MAG: {character['stat_mag']:6d} | MDF: {character['stat_mdf']:6d}\n"
          f"SPD: {character['stat_spd']:6d} | LUK: {character['stat_luk']:6d}\n"
          f"{border}")


def print_corner(row: int, column: int) -> str:
    """
    Print a corner of the board if applicable to row and column.

    :param row: An integer representing the row value on the game board.
    :param column: An integer representing the column value on the game board.
    :precondition: row and column must be integers that are valid row and column values in the game board.
    :postcondition: Determine the character for the room's corner. Return "" if row and column aren't a corner.
    :return: A character representing a corner in the board, or an empty string if it doesn't exist.
    >>> print_corner(0, 0)
    ''
    >>> print_corner(-1, 25)
    '╗'
    """
    if (row, column) == (-1, -1):
        return "╔"
    elif (row, column) == (-1, 25):
        return "╗"
    elif (row, column) == (25, -1):
        return "╚"
    elif (row, column) == (25, 25):
        return "╝"
    return ""


def print_walls(row: int, column: int) -> str:
    """
    Print an inside walls of the board if applicable to row and column.

    :param row: An integer representing the row value on the game board.
    :param column: An integer representing the column value on the game board.
    :precondition: row and column must be integers that are valid row and column values in the game board.
    :postcondition: Determine the string for the room's inside walls. Return "" if row and column aren't an inside wall.
    :return: A string representing a wall in the board, or an empty string if it doesn't exist.
    """
    if (row not in [1, 10, 20] and column in [-1, 25]) or (row, column) == (1, 25) or (row, column) == (10, -1)\
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
    return ""


def print_color(row: int, column: int) -> str:
    """
    Print a colored, movable area if applicable to row and column.

    :param row: An integer representing the row value on the game board.
    :param column: An integer representing the column value on the game board.
    :precondition: row and column must be integers that are valid row and column values in the game board.
    :postcondition: Determine the string for the room's area. Return "" if row and column aren't a movable area.
    :return: A string representing an area in the board, or an empty string if it doesn't exist.
    """
    if 21 <= row <= 24 and column < 4:
        return f"{get_color('c_white')}¤¤¤{get_color('c_reset')}"
    elif (21 <= row <= 24 and 4 <= column <= 24) or (row, column) == (20, 24):
        return f"{get_color('c_magenta')}≡≡≡{get_color('c_reset')}"
    elif 10 <= row <= 19 and column <= 7:
        return f"{get_color('c_yellow')}◊ð≈{get_color('c_reset')}"
    elif 3 <= row <= 9 and 12 <= column <= 24:
        return f"{get_color('c_cyan')}△Λ▴{get_color('c_reset')}"
    elif (row, column) == (1, 24) or 2 <= row <= 19:
        return f"{get_color('c_green')}Îî↑{get_color('c_reset')}"
    elif row == 0:
        return f"{get_color('b_black')}{get_color('c_red')}Ξ♰Ψ{get_color('c_reset')}"
    return ""


def print_room(row: int, column: int, character: dict) -> str:
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
    T - Town (Buy, Inn) [✶□✶]

    :param row: An integer representing the row value on the game board.
    :param column: An integer representing the column value on the game board.
    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: row and column must be integers that are valid row and column values in the game board.
    :precondition: character must be a dictionary with stats and coordinates.
    :return: A string representing the room at (row, column).
    """
    if character['x'] == column and character['y'] == row:
        if row == 0:
            return f"{get_color('b_black')}{get_color('c_blue')}<P>{get_color('c_reset')}"
        return f"{get_color('c_blue')}<P>{get_color('c_reset')}"
    corner = print_corner(row, column)
    if corner != "":
        return corner
    wall = print_walls(row, column)
    if wall != "":
        return wall
    color = print_color(row, column)
    if color != "":
        return color
    return "   "


def print_board(board: dict, character: dict, square_size: int) -> None:
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
    print(f"")
    for row in range(y_top, y_bottom + 1):
        printed_row = ""
        for column in range(x_left, x_right + 1):
            printed_row += print_room(row, column, character)
        print(f"{printed_row}")
    print(board[(character['y'], character['x'])])


def convert_direction_choice(dir_input: str) -> tuple:
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
    >>> convert_direction_choice('p')
    (5, 0)
    >>> convert_direction_choice('buy')
    (6, 0)
    >>> convert_direction_choice('6')
    (6, 0)
    >>> convert_direction_choice('i')
    (0, 0)
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
    elif dir_input in '5p' or dir_input == 'pack':
        dir_movement[0] = 5
    elif dir_input in '6b' or dir_input == 'buy':
        dir_movement[0] = 6
    return tuple(dir_movement)


def print_choices(character: dict, choices_list: list, color_string: str) -> None:
    """
    Print the choices for the user to make when on the map.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param choices_list: A list of strings representing choices for the player.
    :param color_string: A string representing a color to change the terminal text/background to.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: choices_list must be a list containing string choices.
    :precondition: color_string must be a string that can change the terminal text color/background.
    :postcondition: Print the choices for the player to make.
    """
    for index, choice in enumerate(choices_list):
        a_string = f"{index + 1}. ({get_color(color_string)}{choice[0].upper()}{get_color('c_reset')}){choice[1:]}"
        number_of_tabs = f"\t" * (5 - (len(choice) + 1) // 4)
        if color_string == 'c_green':
            item_description = f"\n\t- {get_item(choice.title())['item_description']}"
            a_string += f"{number_of_tabs} Cost: {get_item(choice.title())['item_cost']}{item_description}"
        elif color_string == 'c_cyan':
            item_description = f"\n\t- {get_item(choice.title())['item_description']}"
            a_string += f"{number_of_tabs} ({character['items'][choice.title()]}){item_description}"
        elif choice in ['Double Attack', 'Sword Of Light', 'Heal', 'Fire', 'Critical Slash', 'Analyze']:
            skill = get_skill(character, choice)
            a_string += f"\n\t- {skill['description']}\n\t- MP Cost: {skill['mp_use']}"
        print(a_string)


def at_town(character: dict, options: any) -> any:
    """
    Return town options if player is at a town.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param options: A list or string of options.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Determine if character is at a town, then return town options.
    :return: A list consisting of town options if character is at a town, otherwise an empty list.
    >>> player = make_character()
    >>> options_list = ['north', 'east', 'south', 'west', 'pack']
    >>> options_string = '12345neswp'
    >>> at_town(player, options_list)
    ['north', 'east', 'south', 'west', 'pack']
    >>> at_town(player, options_string)
    '12345neswp'
    >>> player['x'] = 2
    >>> player['y'] = 22
    >>> at_town(player, options_list)
    ['north', 'east', 'south', 'west', 'pack', 'buy', 'inn']
    >>> at_town(player, options_string)
    '1234567neswpbi'
    """
    if (character['x'], character['y']) in [(2, 22), (0, 10), (24, 3)]:
        if type(options) == list:
            options.extend(['buy', 'inn'])
        elif type(options) == str:
            options = options[0:len(options) // 2] + '67' + options[len(options) // 2:len(options)] + 'bi'
    return options


def get_user_choice(character: dict):
    """
    Return the user's coordinate choice.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postconditions: Calculate (x, y)-coordinates depending on user's input.
    :return: Tuple (x, y)-coordinates depending on user's input.
    """
    coordinate_list = at_town(character, ['north', 'east', 'south', 'west', 'pack'])
    print_choices(character, coordinate_list, 'c_blue')
    dir_input = input("Which direction do you want to go? ").lower()
    short_list = at_town(character, '12345neswp')
    while (dir_input not in short_list or (dir_input in short_list and len(dir_input) != 1))\
            and dir_input not in coordinate_list:
        print(f"Invalid input.")
        dir_input = input("Which direction do you want to go? ").lower()
    return dir_input


def is_wall(row: int, column: int, character: dict) -> bool:
    """
    Return whether the player is moving into a wall.

    :param row: A positive integer.
    :param column: A positiver integer.
    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: row and column must be positive integers.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Calculate whether the (row, column) value on the board is a wall.
    :return: A boolean, True if (row, column) is a wall, false otherwise.
    >>> row_y = -1
    >>> column_x = -1
    >>> player = make_character()
    >>> is_wall(row_y, column_x, player)
    True
    >>> row_y = 2
    >>> column_x = 3
    >>> is_wall(row_y, column_x, player)
    False
    """
    wall_strings = ["╔", "╗", "╚", "╝", "║", "╩", "═"]
    for wall_string in wall_strings:
        if wall_string in print_room(row, column, character):
            return True
    return False


def validate_move(board: dict, character: dict, direction: any) -> bool:
    """
    Return whether a player's directional input is possible.

    :param board: A dictionary of the game board.
    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param direction: A string which is the given direction.
    :precondition: board has keys which are tuples of row-column coordinates.
    :precondition: board has values which are coordinate statuses.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: direction is a string and a valid directional input (i.e. in '1234nesw', 'north', 'east', 'south',
                   or 'west').
    :postcondition: Return whether direction on board is valid for character.
    :return: Whether direction on board is valid for character.
    >>> game_board = make_board(25, 25)
    >>> player = make_character()
    >>> move_east = 'e'
    >>> validate_move(game_board, player, move_east)
    True
    >>> move_west = 'w'
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
    not_moving = direction[0] in '0567pbi'
    return (inbound and not wall) or not_moving


def move_character(character: dict, direction: any) -> None:
    """
    Update the character's (x, y)-coordinates.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param direction: A string which is the given direction.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: direction is a string and a valid directional input (i.e. in '1234nesw', 'north', 'east', 'south',
                   or 'west').
    :postcondition: Update character's (x, y)-coordinates via direction.
    """
    direction_tuple = convert_direction_choice(direction)
    character['x'] += direction_tuple[0]
    character['y'] += direction_tuple[1]


def set_skill(skill_name: str, mp_use: int, attack_power: int, defense: any, multiplier: any, description: str,
              battle_text: str) -> dict:
    """
    Return a dictionary for a skill.

    :param skill_name: A string representing the skill's name.
    :param mp_use: A positive integer representing the magic points used up when the skill is used.
    :param attack_power: An integer representing the attack power of the skill.
    :param defense: A string or positive integer representing the defense formula.
    :param multiplier: A number representing the damage multiplier of the skill.
    :param description: A string representing what is shown when seeing the skill in the menu.
    :param battle_text: A string that shows when using the skill in battle
    :precondition: skill_name, description, and battle_text must be strings.
    :precondition: attack must be an integer.
    :precondition: mp_use must be a positive integer.
    :precondition: defense must be a a string representing a valid stat (e.g. 'stat_def') or a positive integer.
    :precondition: multiplier must be a number (integer or float).
    :postcondition: Creates a dictionary for a skill.
    :return: A dictionary containing parameters for a skill.
    """
    skill_dict = {
        'skill_name': skill_name,
        'mp_use': mp_use,
        'atk_power': attack_power,
        'defense': defense,
        'multiplier': multiplier,
        'description': description,
        'battle_text': battle_text
    }
    return skill_dict


def get_defense(defender: dict, skill: dict) -> int:
    """
    Return the defense to be used in the skill calculation.

    :param defender: A dictionary representing either the character or the enemy.
    :param skill: A dictionary representing the skill being used.
    :precondition: defender must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: skill must be a dictionary of a valid in-game skill
    :postcondition: Calculates the defense to use in the attack/skill calculation.
    :return: An integer representing the defense to use in the attack/skill calculation.
    >>> player = make_character()
    >>> enemy = get_enemy('Dream Cell')
    >>> get_defense(enemy, get_skill(player, 'Fire'))
    2
    >>> get_defense(player, get_skill(player, 'Heal'))
    0
    """
    if skill['defense'] == 0:
        return 0
    return defender[skill['defense']]


def get_skill(attacker: dict, skill: str) -> dict:
    """
    Return a skill as a dictionary.

    :param attacker: A dictionary representing either the character or the enemy.
    :param skill: A string representing the skill's name.
    :precondition: attacker must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: skill must be a string.
    :postcondition: Create a dictionary for a skill.
    :return: A dictionary for a skill.
    """
    skills_dict = {
        # Player Skills
        'Double Attack': set_skill(skill,
                                   2,
                                   attacker['stat_atk'],
                                   'stat_def',
                                   3,
                                   'Does twice the damage.',
                                   'attacks the enemy with a strong force'),
        'Sword Of Light': set_skill(skill,
                                    3,
                                    attacker['stat_atk'],
                                    'stat_def',
                                    attacker['stat_max_mp'] / 10 + 2,
                                    'A damage with that gets stronger with a higher MP stat.',
                                    'brings light to their weapon and attacks the enemy with a holy blow'),
        'Heal': set_skill(skill,
                          2,
                          -int(20 + attacker['stat_mag'] / 4),
                          0,
                          1,
                          'Heals the player.',
                          'casts Heal'),
        'Fire': set_skill(skill,
                          2,
                          int(20 + attacker['stat_mag'] / 4),
                          'stat_mdf',
                          1,
                          'Burns the foe with fire.',
                          'casts Fire'),
        'Critical Slash': set_skill(skill,
                                    3,
                                    attacker['stat_atk'],
                                    'stat_def',
                                    2 + attacker['stat_luk'] / 10,
                                    'An attack that increases with the user\'s luck.',
                                    'slashes the enemy with a critical blow'),
        'Enemy Info': set_skill(skill,
                                1,
                                0,
                                0,
                                0,
                                'Gets enemy info for the player.',
                                'analyzes the enemy'),

        # Enemy Skills
        'Bounce': set_skill(skill,
                            0,
                            attacker['stat_atk'],
                            'stat_def',
                            2.5,
                            'Bounce on the enemy.',
                            'bounces high and falls down'),
        'Wait': set_skill(skill,
                          0,
                          0,
                          0,
                          0,
                          'Waits.',
                          'does nothing'),
        'Bite': set_skill(skill,
                          1,
                          attacker['stat_atk'],
                          'stat_def',
                          2.5,
                          'Bite the enemy.',
                          'takes a nice bite of your flesh'),
        'Crawl': set_skill(skill,
                           2,
                           attacker['stat_atk'] + attacker['stat_spd'],
                           'stat_def',
                           1.5,
                           'Crawl on the enemy.',
                           'crawls around on your body, giving you the shivers'),
        'Funky Music': set_skill(skill,
                                 0,
                                 attacker['stat_mag'],
                                 'stat_mdf',
                                 attacker['stat_luk'],
                                 'Play some funky music on the organ.',
                                 'SETS THE BATTLEFIELD ON FIRE WITH HIS EPIC ORGAN CHORDS'),
        'Spike': set_skill(skill,
                           0,
                           attacker['stat_atk'],
                           'stat_def',
                           3,
                           'Attack the enemy with the spikes on your back.',
                           'penetrates with its massive spikes'),
        'Wing Smack': set_skill(skill,
                                1,
                                attacker['stat_atk'] + attacker['stat_mag'] * 0.5,
                                'stat_def',
                                2,
                                'Slam the enemy with wings.',
                                'slams you with its powerful wings'),
        'Roll Around': set_skill(skill,
                                 2,
                                 attacker['stat_hp'],
                                 0,
                                 1,
                                 'Squish the enemy.',
                                 'flattens you like a pancake'),
        '4-Sided Kill': set_skill(skill,
                                  4,
                                  attacker['stat_atk'],
                                  'stat_def',
                                  4,
                                  'Prick the enemy with the four corners.',
                                  'slashes you with its corners'),
        'Soothing Song': set_skill(skill,
                                   4,
                                   attacker['stat_mag'],
                                   'stat_mdf',
                                   attacker['stat_mp'],
                                   'Sing a soothing yet effective song against the enemy.',
                                   'sings its heart out'),
        'Scratch': set_skill(skill,
                             0,
                             attacker['stat_atk'],
                             'stat_def',
                             2.5,
                             'Scratch the opponent.',
                             'scratches you with its claws'),
        'Flee': set_skill(skill,
                          0,
                          0,
                          0,
                          0,
                          'Run away from battle.',
                          'runs away from battle'),
        'Destruction': set_skill(skill,
                                 5,
                                 attacker['stat_hp'] + attacker['stat_atk'],
                                 'stat_def',
                                 2,
                                 'Attack the enemy with a strong blow.',
                                 'plows you with a strong attack'),
        'Death Scare': set_skill(skill,
                                 0,
                                 attacker['stat_atk'] + attacker['stat_mag'],
                                 'stat_def',
                                 3,
                                 'Scare the enemy with its worst nightmares.',
                                 'shocks you with a deadly scare'),
        'Wind': set_skill(skill,
                          4,
                          attacker['stat_mag'],
                          'stat_mdf',
                          2,
                          'Deal wind damage.',
                          'casts Wind'),
        'Blinding Attack': set_skill(skill,
                                     5,
                                     attacker['stat_mag'],
                                     'stat_mdf',
                                     2,
                                     'Blind the enemy with a strong flash of light.',
                                     'flashes you with a strong light spell'),
        'Elemental Freeze': set_skill(skill,
                                      10,
                                      attacker['stat_mag'],
                                      'stat_mdf',
                                      3,
                                      'Attack the enemy with a strong ice attack.',
                                      'conjures up a strong blizzard and blasts you with a sharp, cold freeze'),
        'Dark Shock': set_skill(skill,
                                20,
                                attacker['stat_atk'] + attacker['stat_mag'],
                                0,
                                2,
                                'Send a paralyzing shock to the enemy.',
                                'send a paralyzing shock through your body'),
        'Nightmare Fuel': set_skill(skill,
                                    10,
                                    attacker['stat_mag'],
                                    'stat_mdf',
                                    5,
                                    'Bring the enemy\'s worst nightmares to life.',
                                    'brings your worst nightmares to life, mauling you in the process')
    }
    return skills_dict[skill]


def initialize_class_skills(character: dict) -> None:
    """
    Add skills to character.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Add a skill depending on character's class and subclass.
    """
    for class_type in ['class', 'subclass']:
        if character[class_type] == 'Fighter':
            add_skill(character, 'Double Attack')
        elif character[class_type] == 'Knight':
            add_skill(character, 'Sword Of Light')
        elif character[class_type] == 'Cleric':
            add_skill(character, 'Heal')
        elif character[class_type] == 'Wizard':
            add_skill(character, 'Fire')
        elif character[class_type] == 'Thief':
            add_skill(character, 'Critical Slash')
        elif character[class_type] == 'Robot':
            add_skill(character, 'Enemy Info')


def add_skill(character: dict, skill: str) -> None:
    """
    Add a skill to the character.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param skill: A string representing the skill's name.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: skill must be a string.
    :postcondition: Add skill to character['skills'].
    """
    new_skill = get_skill(character, skill)
    character['skills'].append(new_skill)


def set_item(item_name: str, item_description: str, item_cost: int, item_boost: int, item_stat_boost: list) -> dict:
    """
    Return a dictionary for an item.

    :param item_name: A string representing the item's name.
    :param item_description: A string representing what the item does.
    :param item_cost: A positive integer representing the item's cost at a store.
    :param item_boost: A positive integer representing the amount to heal/boost a stat.
    :param item_stat_boost: A list representing a stat (or stats) to heal/boost.
    :precondition: item_name and item_description must be non-empty strings.
    :precondition: item_cost and item_boost must be positive integers.
    :precondition: item_stat_boost must be a list of a valid stat (or stats) (e.g. 'stat_atk').
    :postcondition: Creates a dictionary for an item.
    :return: A dictionary for an item.
    """
    item_dict = {
        'item_name': item_name,
        'item_description': item_description,
        'item_cost': item_cost,
        'item_boost': item_boost,
        'item_stat_boost': item_stat_boost
    }
    return item_dict


def get_item(item: str) -> dict:
    """
    Return an item as a dictionary.

    :param item: A string representing the item's name.
    :precondition: item must be a string of a valid item.
    :postcondition: Creates a dictionary of item.
    :return: A dictionary of item.
    """
    items_dict = {
        # Regular Items
        'Dream Candy': set_item(item,
                                'Heals 10 HP.',
                                5,
                                10,
                                ['stat_hp']),
        'Water': set_item(item,
                          'Heals 10 MP.',
                          15,
                          10,
                          ['stat_mp']),
        'Vanilla Ice Cream': set_item(item,
                                      'Heals 30 HP.',
                                      12,
                                      30,
                                      ['stat_hp']),
        'Chocolate Sundae': set_item(item,
                                     'Heals 30 MP.',
                                     30,
                                     30,
                                     ['stat_mp']),
        'Super Candy': set_item(item,
                                'Boosts ATK, DEF, MAG, MDF, SPD, and LUK by 2.',
                                100,
                                2,
                                ['stat_atk', 'stat_def', 'stat_mag', 'stat_mdf', 'stat_spd', 'stat_luk'])
    }
    return items_dict[item]


def list_all_lower(string_list: list) -> list:
    """
    Return a list with all elements inside strings of lowercase characters.

    :param string_list: A list with string elements.
    :precondition: string_list must be a list with string elements.
    :postcondition: Make all the strings in string_list lowercase.
    :return: string_list with all strings lowercase.
    >>> list_all_lower([])
    []
    >>> list_all_lower(['HELLO'])
    ['hello']
    >>> list_all_lower(['hello'])
    ['hello']
    >>> list_all_lower(['GOOD', 'bAd', 'okay'])
    ['good', 'bad', 'okay']
    """
    new_string_list = []
    for index, string in enumerate(string_list):
        new_string_list.append(string.lower())
    return new_string_list


def list_to_string_by_first_letter(string_list: list) -> str:
    """
    Return a string to use for input validation.

    :param string_list: A list representing in-game values.
    :precondition: string_list must be a list with strings representing in-game values the player has.
    :postcondition: Creates a string of the list elements.
    :return: A string of the list elements formatted as numbers, then the first character (e.g. '123abc').
    >>> list_to_string_by_first_letter([])
    ''
    >>> list_to_string_by_first_letter(['string'])
    '1s'
    >>> list_to_string_by_first_letter(['hello', 'george'])
    '12hg'
    """
    numbers = ''
    first_letters = ''
    for index, item in enumerate(string_list):
        numbers += str(index + 1)
        first_letters += item[0].lower()
    return numbers + first_letters


def use_item(character: dict, item: str) -> None:
    """
    Run through the process of using an item.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param item: A string representing the input made by the player for the item.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: item must be a string representing a valid in-game item.
    :postcondition: Use item on character.
    """
    item_to_use = get_item(item)
    for index, stat in enumerate(item_to_use['item_stat_boost']):
        character[stat] += item_to_use['item_boost']
        if stat[-2:] in 'hpmp':
            character[f'stat_{stat[-2:]}'] = min(character[f'stat_{stat[-2:]}'], character[f'stat_max_{stat[-2:]}'])
            print(f"You gained {item_to_use['item_boost']} {stat[-2:].upper()} points!")
        else:
            print(f"You gained {item_to_use['item_boost']} {stat[-3:].upper()} points!")
    character['items'][item_to_use['item_name']] -= 1
    if not character['items'][item_to_use['item_name']]:
        character['items'].pop(item_to_use['item_name'])


def get_lower(string):
    """
    Return the string but lowercase.

    :param string: A string.
    :precondition: string must be a string.
    :postcondition: Get the lowercase version of string.
    :return: The lowercase of string.
    >>> get_lower('')
    ''
    >>> get_lower('hi')
    'hi'
    >>> get_lower('HELLO')
    'hello'
    """
    return string.lower()


def select_item(character: dict) -> any:
    """
    Select item to use.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Choose the item character will use (or None for invalid inputs).
    :return: A string representing the item's name, or None if an invalid input was given.
    """
    if len(character['items']):
        sorted_items = list(map(get_lower, sorted(list(character['items'].keys()))))
        print_choices(character, sorted_items, 'c_cyan')
        short_sorted_items = list_to_string_by_first_letter(sorted_items)
        item_input = input(f"Which item do you want to use? ").lower()
        if (item_input not in short_sorted_items or (item_input in short_sorted_items and len(item_input) != 1))\
                and item_input not in sorted_items:
            return None
        else:
            item_input = convert_short_input(item_input, short_sorted_items, sorted_items).title()
            return item_input
    else:
        print(f"Your pack is empty!")


def pack(character: dict) -> None:
    """
    Check the pack.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Use the item if applicable.
    """
    item_input = select_item(character)
    if item_input:
        use_item(character, item_input)


def get_shop(character: dict) -> list:
    """
    Return the shop the player is at.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Create a list of items to buy depending on character's location.
    :return: A list of items depending on character's location.
    """
    if character['x'] == 24:
        print(f"Welcome to 'I've Been Chilling' Ice Cream Parlor!")
        return ['vanilla Ice Cream', 'chocolate Sundae']
    print(f"Welcome to my shop!")
    return ['dream Candy', 'water']


def checkout(character: dict, buy_input: str) -> None:
    """
    Run through process of buying the item (if possible).

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param buy_input: A string representing the item the player wants to buy.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: buy_input must be a string of a valid in-game item.
    :postcondition: Check if the item can be bought, and add it to character's inventory if so.
    """
    item_to_buy = get_item(buy_input)
    if character['money'] >= item_to_buy['item_cost']:
        character['money'] -= item_to_buy['item_cost']
        if buy_input not in character['items'].keys():
            character['items'][buy_input] = 0
        character['items'][buy_input] += 1
        print(f"You just bought a {buy_input}. Have a good day!")
    else:
        print(f"Sorry, {character['name']}. I can't give credit. Come back when you're a little...MMM...richer!")


def buy(character: dict) -> None:
    """
    Run through buying an item.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :return: What character has bought
    """
    shop_items = get_shop(character)
    print_choices(character, shop_items, 'c_green')
    buy_input = input(f"What do you want to buy? ").lower()
    short_shop_items = '12' + shop_items[0][0] + shop_items[1][0]
    if (buy_input not in short_shop_items or (buy_input in short_shop_items and len(buy_input) != 1))\
            and buy_input not in shop_items:
        print(f"Have a good day!")
    else:
        buy_input = convert_short_input(buy_input, short_shop_items, shop_items).title()
        checkout(character, buy_input)


def inn(character: dict) -> None:
    """
    Check the inn.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Go through
    """
    inn_input = input("Wanna stay at the inn? ").lower()
    if (inn_input not in 'yn' or (inn_input in 'yn' and len(inn_input) != 1)) and inn_input not in ['yes', 'no']:
        print(f"Have a good day!")
    else:
        print(f"You rest at the inn, restoring your health and magic.\n")
        character['stat_hp'] = character['stat_max_hp']
        character['stat_mp'] = character['stat_max_mp']
        print_character_stats(character)
        sleep_paralysis_demon = random.randint(0, 99)
        if not sleep_paralysis_demon:
            print(f"- But you suddenly wake up in the middle of the night to an ominous creature standing before you.\n"
                  f"- It's...your sleep paralysis demon, here to take your life.")
            battle(character, get_enemy('Sleep Paralysis Demon'))


def perform_character_action(character: dict, direction: any) -> None:
    """

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param direction: A string which is the given direction.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: direction is a string and a valid directional input (i.e. in '1234nesw', 'north', 'east', 'south',
                   or 'west').
    :postcondition: Move the character, check items, buy, or sleep.
    """
    if direction[0] in '5p':
        pack(character)
    elif direction[0] in '6b':
        buy(character)
    elif direction[0] in '7i':
        inn(character)
    else:
        move_character(character, direction)


def check_for_foes() -> bool:
    """
    Return whether a foe appears or not (20% chance it does).

    :return: A boolean (True 20% of the time).
    """
    foe_exists = random.randint(0, 4)
    return not foe_exists


def set_enemy(enemy_name: str, enemy_hp: int, enemy_mp: int, enemy_atk: int, enemy_def: int, enemy_mag: int,
              enemy_mdf: int, enemy_spd: int, enemy_luk: int, enemy_skills: list, enemy_exp: int, enemy_money: int)\
        -> dict:
    """
    Return a dictionary for an enemy.

    :param enemy_name: A string representing the enemy's name.
    :param enemy_hp: A positive integer representing the enemy's health points.
    :param enemy_mp: A positive integer representing the enemy's magic points.
    :param enemy_atk: A positive integer representing the enemy's attack.
    :param enemy_def: A positive integer representing the enemy's defense.
    :param enemy_mag: A positive integer representing the enemy's magic attack.
    :param enemy_mdf: A positive integer representing the enemy's magic defense.
    :param enemy_spd: A positive integer representing the enemy's speed.
    :param enemy_luk: A positive integer representing the enemy's luck.
    :param enemy_skills: A list of skills the enemy can use (either than a regular attack).
    :param enemy_exp: A positive integer representing the experience points the enemy gives out.
    :param enemy_money: A positive integer representing the money the enemy gives out.
    :precondition: enemy_name must be a string.
    :precondition: enemy_skills must be a list with each element a valid skill dictionary.
    :precondition: Every parameter sans enemy_name and enemy_skills must be a positive integer (I do not plan on typing
                   them all out).
    :postcondition: Creates a dictionary for an enemy.
    :return: A dictionary for an enemy.
    """
    enemy_dict = {
        'name': enemy_name,
        'stat_hp': enemy_hp,
        'stat_max_hp': enemy_hp,
        'stat_mp': enemy_mp,
        'stat_max_mp': enemy_mp,
        'stat_atk': enemy_atk,
        'stat_def': enemy_def,
        'stat_mag': enemy_mag,
        'stat_mdf': enemy_mdf,
        'stat_spd': enemy_spd,
        'stat_luk': enemy_luk,
        'skills': enemy_skills,
        'exp': enemy_exp,
        'money': enemy_money
    }
    return enemy_dict


def get_enemy(enemy: str) -> dict:
    """
    Return an enemy as a dictionary.

    :param enemy: A string representing the enemy's name.
    :precondition: enemy must be a string containing a valid in-game enemy.
    :postcondition: Creates a dictionary for the enemy with stats.
    :return: A dictionary with for the enemy with stats.
    """
    enemies_dict = {
        # Regular Enemies
        'Dream Cell': set_enemy(enemy, 10, 2, 2, 2, 2, 2, 2, 2, ['Bounce', 'Wait'], 5, 2),  # 1M
        'Spider': set_enemy(enemy, 15, 3, 3, 1, 2, 1, 4, 5, ['Bite', 'Crawl'], 8, 6),  # 1M
        'Organ Man': set_enemy(enemy, 30, 20, 3, 2, 3, 2, 1, 3, ['Funky Music'], 20, 12),  # 123F
        'Dream Shell': set_enemy(enemy, 20, 5, 4, 6, 4, 6, 2, 2, ['Spike'], 12, 6),  # M
        'Giant Moth': set_enemy(enemy, 35, 20, 5, 4, 10, 8, 6, 6, ['Wing Smack'], 15, 10),  # M
        'Dream Swell': set_enemy(enemy, 25, 8, 3, 15, 15, 3, 3, 3, ['Roll Around'], 16, 8),  # 2
        'Floating Square': set_enemy(enemy, 32, 16, 8, 12, 8, 8, 12, 4, ['4-Sided Kill'], 24, 12),  # 2
        'Dream Bell': set_enemy(enemy, 35, 20, 6, 20, 20, 12, 10, 30, ['Soothing Song'], 27, 12),  # 3
        'Mountain Lion': set_enemy(enemy, 40, 10, 7, 7, 5, 7, 10, 10, ['Scratch'], 20, 15),  # 3
        'Golden Ticket': set_enemy(enemy, 5, 5, 5, 5, 5, 5, 5, 5, ['Flee'], 200, 200),  # 3
        'Dream Hell': set_enemy(enemy, 50, 10, 12, 12, 8, 12, 16, 20, ['Destruction'], 25, 16),  # F
        'Eerie Ghost': set_enemy(enemy, 75, 20, 25, 5, 25, 5, 30, 50, ['Death Scare'], 40, 40),  # F

        # Bosses
        'Straw Beast': set_enemy(enemy, 40, 10, 4, 3, 5, 5, 8, 12, ['Wind'], 50, 40),  # First Boss
        'Void': set_enemy(enemy, 75, 20, 8, 10, 12, 10, 12, 20, ['Blinding Attack'], 125, 100),  # Colorless Boss
        'Dark Lord': set_enemy(enemy, 120, 80, 10, 15, 18, 15, 15, 15, ['Elemental Freeze'], 300, 225),  # Mountain Boss
        'Sleep Paralysis Demon': set_enemy(enemy, 1000, 1000, 200, 100, 200, 100, 350, 500, ['Dark Shock'], 10000,
                                           10000),  # Hidden boss that appears 1% of the time at the inn
        'Dream Demon': set_enemy(enemy, 200, 200, 20, 20, 20, 20, 20, 20, ['Nightmare Fuel'], 0, 0)  # Final Boss
    }
    return enemies_dict[enemy]


def generate_first_area_enemies(column: int) -> dict:
    """
    Generate enemies from the first area of the game.

    :param column: An integer representing the column value on the game board.
    :precondition: column must be an integer that is a valid column value in the game board.
    :postcondition: Generate an enemy dictionary given column.
    :return: An enemy as a dictionary.
    """
    if 4 <= column <= 13:
        return get_enemy('Dream Cell')
    enemy_generated = random.randint(0, 1)
    if enemy_generated:
        return get_enemy('Dream Cell')
    return get_enemy('Spider')


def generate_second_area_enemies(row: int) -> dict:
    """
    Generate enemies from the second (colorless) area of the game.

    :param row: An integer representing the row value on the game board.
    :precondition: row must be an integer that is a valid row value in the game board.
    :postcondition: Generate an enemy dictionary given row.
    :return: An enemy as a dictionary.
    """
    if row <= 15:
        return get_enemy('Dream Swell')
    enemy_generated = random.randint(0, 1)
    if enemy_generated:
        return get_enemy('Dream Swell')
    return get_enemy('Floating Square')


def generate_third_area_enemies(row: int, column: int) -> dict:
    """
    Generate enemies from the third (mountains) area of the game.

    :param row: An integer representing the row value on the game board.
    :param column: An integer representing the column value on the game board.
    :precondition: row and column must be integers that are valid row and column values in the game board.
    :postcondition: Generate an enemy dictionary given row and column.
    :return: An enemy as a dictionary.
    """
    if (row, column) == (6, 21):
        return get_enemy('Golden Ticket')
    enemy_generated = random.randint(0, 4)
    if enemy_generated <= 2:
        return get_enemy('Dream Bell')
    return get_enemy('Mountain Lion')


def generate_main_area_enemies() -> dict:
    """
    Generate enemies from the main area of the game.

    :return: An enemy as a dictionary.
    """
    enemy_generated = random.randint(0, 9)
    if enemy_generated <= 1:
        return get_enemy('Dream Cell')
    elif enemy_generated <= 6:
        return get_enemy('Spider')
    elif enemy_generated <= 8:
        return get_enemy('Dream Shell')
    return get_enemy('Giant Moth')


def generate_final_area_enemies() -> dict:
    """
    Generate enemies from the final (dark world) area of the game.

    :return: An enemy as a dictionary.
    """
    enemy_generated = random.randint(0, 9)
    if enemy_generated <= 2:
        return get_enemy('Dream Hell')
    return get_enemy('Eerie Ghost')


def generate_enemy(row: int, column: int) -> any:
    """
    Return the enemy to fight against the player.

    :param row: An integer representing the row value on the game board.
    :param column: An integer representing the column value on the game board.
    :precondition: row and column must be integers that are valid row and column values in the game board.
    :postcondition: Generate an enemy dictionary given row and column.
    :return: An enemy as a dictionary.
    """
    if 21 <= row <= 24 and column < 4:  # First area of the game, shouldn't generate any enemies (white)
        return None
    elif (21 <= row <= 24 and 4 <= column <= 24) or (row, column) == (20, 24):  # First area (magenta)
        return generate_first_area_enemies(column)
    elif 11 <= row <= 19 and column <= 7:  # Second area (yellow)
        return generate_second_area_enemies(row)
    elif 3 <= row <= 9 and 12 <= column <= 24:  # Third area (cyan)
        return generate_third_area_enemies(row, column)
    elif (row, column) == (1, 24) or 2 <= row <= 19:  # Main area (green)
        return generate_main_area_enemies()
    elif row == 0:  # Final area (black/red)
        return generate_final_area_enemies()


def check_critical_chance(critical_chance: int) -> any:
    """
    Return the critical hit multiplier to the attack.

    :param critical_chance: An integer representing if the attack is a critical hit.
    :precondition: critical_chance must be an integer >= 0.
    :postcondition: Calculate the critical hit multiplier if the attack is a critical hit.
    :return: A float, representing the number to multiply to the initial attack value.
    """
    if not critical_chance:
        critical_base = 1.5
        critical_slope = 0.5
        critical_variance = critical_slope * random.random() + critical_base
        print(f"{get_color('c_yellow')}A critical hit!{get_color('c_reset')}")
        return critical_variance
    return 1


def print_damage_output(attacker: dict, defender: dict, damage: int) -> None:
    """
    Print the amount of damage dealt/healed after attacking/using a skill.

    :param attacker: A dictionary representing either the character or the enemy.
    :param defender: A dictionary representing either the character or the enemy.
    :param damage: A integer representing the amount of damage the defender will receive.
    :precondition: attacker must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: defender must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: One of attacker/defender must be the character dictionary, with the other being the enemy dictionary.
    :precondition: defender must be an integer.
    :postcondition: Print the amount of damage dealt/healed after attacker uses a skill (heal if attacker is defender,
                    deal otherwise).
    """
    if attacker == defender:
        print(f"{attacker['name']} heals {-1 * damage} points of damage!")
    else:
        print(f"{attacker['name']} deals {damage} points of damage!")


def select_battle_input(character: dict) -> str:
    """
    Select option to use in battle.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Choose the input character will use in battle.
    :return: The input to choose in battle as a string.
    """
    battle_input_list = ['attack', 'skill', 'item', 'flee']
    print_choices(character, battle_input_list, 'c_red')
    # Give player options for turn (attack, skill, run)
    battle_input = input("What will you do this turn? ").lower()
    short_battle_input = list_to_string_by_first_letter(battle_input_list)
    while (battle_input not in short_battle_input or (battle_input in short_battle_input and len(battle_input) != 1)) \
            and battle_input not in battle_input_list:
        invalid_input(short_battle_input)
        battle_input = input("What will you do this turn? ").lower()
    battle_input = convert_short_input(battle_input, short_battle_input, battle_input_list).title()
    return battle_input


def get_dictionary_keys(dictionary_list: list, dictionary_key: any) -> list:
    """
    Return the dictionary keys as a list (if multiple dictionaries are in one list).

    :param dictionary_list: A list consisting of dictionaries.
    :param dictionary_key: A value that is a valid dictionary key.
    :precondition: dictionary_list must be a list of dictionaries that all have the same keys.
    :precondition: dictionary_key must be a valid key in a dictionary in dictionary_list.
    :postcondition: Creates a list of given dictionary_key from dictionary_list.
    :return: A list of dictionary_key of dictionary_list.
    """
    dictionary_keys = []
    for dictionary in dictionary_list:
        dictionary_keys.append(dictionary[dictionary_key])
    return dictionary_keys


def select_skill(character: dict) -> any:
    """
    Select skill to use in battle.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Choose the skill character will use in battle.
    :return: The skill to choose in battle as a skill dictionary.
    """
    if character['skills']:
        skill_names = list_all_lower(get_dictionary_keys(character['skills'], 'skill_name'))
        print_choices(character, get_dictionary_keys(character['skills'], 'skill_name'), 'c_red')
        skill_input = input("Which skill will you use? ").lower()
        short_skill_input = list_to_string_by_first_letter(skill_names)
        if (skill_input not in short_skill_input or (skill_input in short_skill_input and len(skill_input) != 1)) \
                and skill_input not in skill_names:
            return None
        skill_input = convert_short_input(skill_input, short_skill_input, skill_names).title()
        return skill_input
    else:
        print(f"You don't have any skills!")


def use_skill(attacker: dict, defender: dict, skill: dict) -> None:
    """
    Return skill damage/healing in battle.

    :param attacker: A dictionary representing either the character or the enemy.
    :param defender: A dictionary representing either the character or the enemy.
    :param skill: A dictionary representing the skill being used.
    :precondition: attacker must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: defender must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: skill must be a formatted skill dictionary.
    :precondition: One of attacker/defender must be the character dictionary, with the other being the enemy dictionary.
    :postcondition: Calculate the damage/healing to deal in battle as an integer.
    :return: An integer, the damage the defender will receive (or health the attacker will gain).
    """
    base = 0.8
    slope = 0.4
    random_number = slope * random.random() + base
    skill_damage = (skill['atk_power'] * skill['multiplier'] - get_defense(defender, skill)) * random_number
    print(f"{attacker['name']} {skill['battle_text']}!")
    if attacker != defender:  # No need to critical hit for a skill like Heal
        critical_chance = random.randint(0, max(0, int(20 - attacker['stat_luk'] / 50)))
        skill_damage *= check_critical_chance(critical_chance)
        skill_damage = max(0, skill_damage)
    skill_damage = int(skill_damage)
    defender['stat_hp'] -= skill_damage
    defender['stat_hp'] = min(defender['stat_hp'], defender['stat_max_hp'])  # No healing above maximum HP
    defender['stat_hp'] = max(0, defender['stat_hp'])  # No going below 0 HP
    attacker['stat_mp'] = max(0, attacker['stat_mp'] - skill['mp_use'])
    print_damage_output(attacker, defender, skill_damage)


def attack(attacker: dict, defender: dict) -> None:
    """
    Return attack damage in battle.

    :param attacker: A dictionary representing either the character or the enemy.
    :param defender: A dictionary representing either the character or the enemy.
    :precondition: attacker must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: defender must be a dictionary with stats (and (x, y)-coordinates if the character).
    :precondition: One of attacker/defender must be the character dictionary, with the other being the enemy dictionary.
    :postcondition: Calculate the damage to deal in battle as an integer.
    :return: An integer, the damage the defender will receive.
    """
    multiplier = 2
    if 'class' in attacker.keys() and attacker['class'] == 'fighter':
        multiplier = 2.5
    base = 0.8
    slope = 0.4
    random_number = slope * random.random() + base  # Generate a random number in between base and base + slope
    critical_chance = random.randint(0, max(0, int(20 - attacker['stat_luk'] / 50)))
    attack_damage = (attacker['stat_atk'] * multiplier - defender['stat_def']) * random_number
    print(f"{attacker['name']} attacks!")
    attack_damage *= check_critical_chance(critical_chance)
    attack_damage = max(0, int(attack_damage))
    defender['stat_hp'] -= attack_damage
    defender['stat_hp'] = min(defender['stat_hp'], defender['stat_max_hp'])  # No healing above maximum HP
    defender['stat_hp'] = max(0, defender['stat_hp'])  # No going below 0 HP
    print_damage_output(attacker, defender, attack_damage)


def level_up(character: dict) -> bool:
    """
    Return whether a character can level up.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Determine if character['exp'] is enough to increase character['level'] by 1 (True if so, otherwise
                    False).
    :return: A boolean, whether character can level up.
    """
    next_level = 16 * character['level']**2 - 13 * character['level'] + 7  # Experience equation
    next_level_exp_needed = max(0, next_level - character['exp'])
    print(f"{next_level_exp_needed} experience points until {character['level'] + 1}!")
    return character['exp'] >= next_level


def class_stat_change(stat: str, character: dict, class_type: str) -> int:
    """
    Return the amount of points being added depending on the character's class and subclass.

    :param stat: A string representing a valid stat.
    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param class_type: A string representing either the character's class or subclass.
    :precondition: stat must be a valid stat ('hp', 'mp', 'atk', 'def', 'mag', 'mdf', 'spd', 'luk').
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: class_type must be a string of either 'class' or 'subclass'.
    :postcondition: Calculate an integer to add to stat for character depending on class_type.
    :return: An integer which is added to stat for character depending on class_type.
    """
    if (stat == 'hp' and character[class_type] in ['Knight', 'Robot'])\
            or (stat == 'mp' and character[class_type] in ['Cleric', 'Wizard'])\
            or (stat == 'atk' and character[class_type] in ['Fighter', 'Knight'])\
            or (stat == 'def' and character[class_type] in ['Knight', 'Robot'])\
            or (stat == 'mag' and character[class_type] in ['Cleric', 'Wizard'])\
            or (stat == 'mdf' and character[class_type] in ['Cleric', 'Wizard'])\
            or (stat == 'spd' and character[class_type] in ['Fighter', 'Thief'])\
            or (stat == 'luk' and character[class_type] in ['Fighter', 'Thief']):
        if class_type == 'class':
            return random.randint(4, 5)
        return random.randint(2, 3)
    return random.randint(0, 1)


def stat_change(stat: str, character: dict) -> int:
    """
    Return the amount of points to add to a character's stat.

    :param stat: A string representing a valid stat.
    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: stat must be a valid stat ('hp', 'mp', 'atk', 'def', 'mag', 'mdf', 'spd', 'luk').
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Calculate an integer to add to stat for character.
    :return: A integer which is added to stat for character.
    """
    class_increase = class_stat_change(stat, character, 'class')
    subclass_increase = class_stat_change(stat, character, 'subclass')
    return class_increase + subclass_increase


def bonus_stats(character: dict) -> None:
    """
    Add stats to the character when leveling up.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :precondition: character must be a dictionary with stats and coordinates.
    :postcondition: Add bonus stats to character depending on class and subclass.
    """
    character['level'] += 1
    print(f"\n{character['name']} has reached level {character['level']}!")
    stats = ['hp', 'mp', 'atk', 'def', 'mag', 'mdf', 'spd', 'luk']
    for stat in stats:
        stat_increase = stat_change(stat, character)
        print(f"{character['name']}'s {stat.upper()} increased by {stat_increase}!")
        if stat in 'hpmp':  # Increase maximum HP along with current HP
            character['stat_max_' + stat] += stat_increase
        character['stat_' + stat] += stat_increase


def post_battle(character: dict, enemy: dict) -> bool:
    """
    Do post-battle events, like gaining experience and money, and also leveling up.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param enemy: A dictionary representing the enemy's stats.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: enemy must be a dictionary with stats.
    :postcondition: Run through post-battle events.
    """
    character['exp'] += enemy['exp']
    character['money'] += enemy['money']
    print(f"{character['name']} gained {enemy['exp']} experience points!")
    print(f"{character['name']} gained {enemy['money']} money!")
    if level_up(character):
        bonus_stats(character)
        return True
    return False


def battle(character: dict, enemy: dict) -> None:
    """
    Run through the battle's logic, and end it when either the character or the enemy dies.

    :param character: A dictionary representing the character's stats and (x, y)-coordinates.
    :param enemy: A dictionary representing the enemy's stats.
    :precondition: character must be a dictionary with stats and coordinates.
    :precondition: enemy must be a dictionary with stats.
    :postcondition: Run through the battle and end it when either character['stat_hp'] or enemy['stat_hp'] is 0.
    """
    print(f"\n{enemy['name']} wants to fight!")
    while True:
        battle_input = select_battle_input(character)
        skill_input = ''
        item_input = ''
        while True:
            if battle_input == 'Attack':
                break
            elif battle_input == 'Skill':
                skill_input = select_skill(character)
                if skill_input not in get_dictionary_keys(character['skills'], 'skill_name'):
                    battle_input = select_battle_input(character)
                elif get_skill(character, skill_input)['mp_use'] > character['stat_mp']:
                    print(f"Your MP is too low!")
                    battle_input = select_battle_input(character)
                else:
                    break
            elif battle_input == 'Item':
                item_input = select_item(character)
                if item_input not in character['items'].keys():
                    battle_input = select_battle_input(character)
                else:
                    break
            elif battle_input == 'Flee' and enemy['name'] not in ['Organ Man', 'Straw Beast', 'Void', 'Dark Lord',
                                                                  'Sleep Paralysis Demon', 'Dream Demon']:
                print(f"{character['name']} escapes!")
                return None
            else:
                print(f"What are you doing!? You can't run away from these fights!")
                battle_input = select_battle_input(character)
        # Determine turn order
        player_attacking = character['stat_spd'] > enemy['stat_spd']
        if character['stat_spd'] == enemy['stat_spd']:
            player_attacking = not random.randint(0, 1)
        actions_left = 2
        while actions_left:
            if player_attacking:
                if battle_input == 'Attack':
                    attack(character, enemy)
                elif battle_input == 'Skill' and skill_input == 'Heal':
                    use_skill(character, character, get_skill(character, skill_input))
                elif battle_input == 'Skill':
                    use_skill(character, enemy, get_skill(character, skill_input))
                elif battle_input == 'Item':
                    use_item(character, item_input)
                if enemy['stat_hp'] == 0:
                    print(f"You won!")
                    post_battle(character, enemy)
                    return None
            else:
                use = enemy['skills'][random.randint(0, len(enemy['skills']) - 1)]
                enemy_skill = get_skill(enemy, use)
                enemy_attack = random.randint(0, 1)
                if enemy_attack or enemy_skill['mp_use'] > enemy['stat_mp']:
                    attack(enemy, character)
                else:
                    use_skill(enemy, character, enemy_skill)
                if character['stat_hp'] == 0:
                    game_over()
            player_attacking = not player_attacking
            actions_left -= 1
        print(f"Your HP: {character['stat_hp']}/{character['stat_max_hp']}")
        print(f"Your MP: {character['stat_mp']}/{character['stat_max_mp']}")
        print(f"Enemy's HP: {enemy['stat_hp']}/{enemy['stat_max_hp']}")
        print(f"Enemy's MP: {enemy['stat_mp']}/{enemy['stat_max_mp']}")


def game_over() -> None:
    """
    Run through the game over sequence.
    """
    print(f"Unfortunately for you, were were unable to wake up. You live in the dream world forever.\nGAME OVER!!!")
    sys.exit()


def game() -> None:
    """
    Run through the game's logic.
    """
    # ~~~ Set variables ~~~
    rows = 25
    columns = 25
    board = make_board(rows, columns)
    character = make_character()
    selecting_subclass = False
    # INTRO FUNCTION
    intro()
    character['name'] = set_name()
    character['class'] = set_class(selecting_subclass)
    set_class_bonus(character, 'class')
    selecting_subclass = True
    character['subclass'] = set_class(selecting_subclass)
    if character['subclass'] == character['class']:
        print(f"\nThat's already your main class. Please choose again.")
        character['subclass'] = set_class(selecting_subclass)
    set_class_bonus(character, 'subclass')
    initialize_class_skills(character)
    print(f"- With the information you have in your hand, you feel ready to conquer whatever's in front of you.\n"
          f"- As a hint, the first town is 2 east, then two north. Use it as a reference. Other towns are right by\n"
          f"  a noticable area.\n"
          f"- Go forth...and have fun!")
    print_character_stats(character)
    events = switch_statements()
    check_events(character, events)
    valid_move = False  # Added here so I don't output the map twice.
    square_size = 7
    while character['stat_hp'] > 0 and not events['boss_final']:
        if not valid_move:  # Added here so I don't output the map twice.
            print_board(board, character, square_size)
        direction = get_user_choice(character)
        valid_move = validate_move(board, character, direction)
        if valid_move:
            perform_character_action(character, direction)
            print_board(board, character, square_size)
            check_events(character, events)
            if events['boss_final']:
                break
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger and direction[0] not in '5p':
                enemy = generate_enemy(character['y'], character['x'])
                if enemy is not None:
                    battle(character, enemy)
                    print_character_stats(character)
        else:
            print(f"Can't move here.")
    number_left = 41
    for index in itertools.cycle('~.^.'):
        print(index, end='')
        number_left -= 1
        if not number_left:
            break
    print(f"You beat the game!\nCONGRATULATIONS!")


def main() -> None:
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
