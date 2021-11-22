from unittest import TestCase
from unittest.mock import patch
from game import intro
import io


class TestIntro(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_intro(self, mock_output):
        expected = f"- You find yourself waking up in a quiet area that you can't seem to recognize. Slowly picking " \
                   f"yourself\n"\
                   f"  off the ground, the surrounding area is a clear, white abyss. Almost nothing to the eye.\n"\
                   f"- From your left, someone walks by and stops beside you. He has a large straw hat on, but you " \
                   f"can't see\n"\
                   f"  his eyes. Turning over to you, he begins to speak.\n"\
                   f"???: He got you too, didn't he?\n"\
                   f"- But you don't know what he's talking about. 'He got you too'? What happened when you fell " \
                   f"asleep?\n"\
                   f"???: I've been trying to find a cure to wake myself up, but I heard the only way to get it is by " \
                   f"kiiling\n"\
                   f"     the Dream Demon. But nobody's been strong enough to face off against him. They all become " \
                   f"obstacles\n"\
                   f"     for the rest of us who fight to open our eyes once again.\n"\
                   f"- Without a word, he walks off, leaving you there to ponder over what happened. You try to " \
                   f"remember bits\n"\
                   f"  and pieces about yourself, but only come up with your name.\n"\
                   f"- So...who are you, anyways?\n"
        intro()
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
