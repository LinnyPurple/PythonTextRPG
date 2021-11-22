from unittest import TestCase
from unittest.mock import patch
from game import make_character, switch_statements, check_town_events
import io


class TestCheckTownEvents(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_town_events_no_town(self, mock_output):
        character = make_character()
        events = switch_statements()
        character['x'] = 0
        character['y'] = 0
        expected = ''
        check_town_events(character, events)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_town_events_first_town_print(self, mock_output):
        character = make_character()
        events = switch_statements()
        character['x'] = 2
        character['y'] = 22
        expected = f"- Welcome to the first town of the game!\n"\
                   f"- Here, you can buy items and sleep at the inn.\n\n"
        check_town_events(character, events)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_check_town_events_first_town_first_visit_true(self):
        character = make_character()
        events = switch_statements()
        character['x'] = 2
        character['y'] = 22
        expected = True
        check_town_events(character, events)
        actual = events['first_town_first_visit']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_town_events_colorless_town_print(self, mock_output):
        character = make_character()
        events = switch_statements()
        character['x'] = 0
        character['y'] = 10
        expected = f"- As you enter this new town, you notice instantly how...colorless the town is. White and black " \
                   f"as\n"\
                   f"  far as the eye can see. You take a look at yourself...you still have the color on your body. " \
                   f"So\n"\
                   f"  what happened?\n"\
                   f"- You see someone come up to you, someone void of color. He looks sad.\n"\
                   f"???: Hey. You an outsider?\n"\
                   f"- You nod hesitantly. His voice is sharp like a large blade.\n"\
                   f"J: The name's J. I built this town with my bare hands, but overnight, the color just...poof! " \
                   f"Gone!\n"\
                   f"   Ya look like someone who could help bring it back. Could ya do it for me?\n"\
                   f"- He casually cracks his fingers, making you nod in response.\n"\
                   f"J: I'm certain there's something to bring the color back around here somewhere...a dark, " \
                   f"sinister\n"\
                   f"   creature came by here once, making the rest of the townsfolk cower in fear. I'll give ya a " \
                   f"nice\n"\
                   f"   reward if ya can bring my town back to life!\n"
        check_town_events(character, events)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_check_town_events_colorless_town_first_visit_true(self):
        character = make_character()
        events = switch_statements()
        character['x'] = 0
        character['y'] = 10
        expected = True
        check_town_events(character, events)
        actual = events['colorless_first_visit']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_town_events_mountains_town_print(self, mock_output):
        character = make_character()
        events = switch_statements()
        character['x'] = 24
        character['y'] = 3
        expected = f"- The grassy terrain changes into one of thick, white snow. Your feet sink into the snow, leaving " \
                   f"a\n"\
                   f"  noticeable footprint with each step you take. Colorful lights are strung along the walls of " \
                   f"every\n"\
                   f"  house, each one a quaint little wooden cabin. You feel like you could live here for a long " \
                   f"time.\n"\
                   f"- Suddenly, you see something gracefully walk across the snow: a bipedal panda, only six inches " \
                   f"tall.\n"\
                   f"  It's wearing a pink, blue and white cloth around its body, and stops right by your feet.\n"\
                   f"Panda: OH MY GOSH!\n"\
                   f"- Staring up at you, the panda climbs up your leg and up your torso. Trying to remove it from " \
                   f"your\n"\
                   f"  body doesn't do anything, allowing it to climb up to your face. Once there, it positions " \
                   f"itself\n"\
                   f"  and begins to boop you on the nose with immense speed. Even though the panda is blocking your " \
                   f"view,\n"\
                   f"  it feels quite nice to have a soft, fluffy panda comforting you in such a way.\n"\
                   f"???: Ahem!\n"\
                   f"- A loud cough comes from in front of you, and the panda stops booping. It turns around and " \
                   f"jumps off\n"\
                   f"  you in shock.\n"\
                   f"Panda: MAMA!\n"\
                   f"???: Ali, what did we say about booping strangers?\n"\
                   f"Ali: But mama...they looked very cold!\n"\
                   f"???: I know, I know.\n"\
                   f"- The black-haired woman takes the panda and lets it rest on her shoulder.\n"\
                   f"Katt: I'm sorry...{character['name']}, thanks. I'm Katt, the mayor of this town. Ali here is a\n"\
                   f"      little...what should I say? ...Fiesty.\n"\
                   f"Ali: I am NOT, mama!\n"\
                   f"- Katt chuckles at Ali's reaction.\n"\
                   f"Katt: Though she has been a little more...upset, so to speak.\n"\
                   f"Ali: Yeah! Greystone's nose has disappeared!\n"\
                   f"Katt: Greystone's one of her best friends. A much smaller panda. He woke up one day without his\n"\
                   f"      nose, and his fur has slowly been coming off.\n"\
                   f"Ali: Can you please help find it? I don't want his fur to go away!\n"\
                   f"- Ali cowers her head. You feel guilty and accept their request.\n"\
                   f"Katt: A group of theives have been stealing things and head off to the farthest mountains. I'm\n"\
                   f"      certain they've went there. We wish you the best of luck!\n"
        check_town_events(character, events)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_check_town_events_mountains_town_first_visit_true(self):
        character = make_character()
        events = switch_statements()
        character['x'] = 24
        character['y'] = 3
        expected = True
        check_town_events(character, events)
        actual = events['mountains_first_visit']
        self.assertEqual(expected, actual)
