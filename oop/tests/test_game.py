import unittest
from oop.sports import *


class TestGame(unittest.TestCase):

    def test_white_differs_from_black(self):
        white = Player("Jan Kowalski", 1200)
        black = Player("Jan Nowak", 1200)

        game = Game(white, black, 1)

        self.assertEqual(game.white, white)
        self.assertEqual(game.black, black)
        self.assertNotEqual(game.white, game.black)

    def test_white_won_returns_correct_value(self):
        white = Player("Jan Kowalski", 1200)
        black = Player("Jan Nowak", 1200)

        game = Game(white, black, 1)

        self.assertTrue(game.white_won())
        self.assertFalse(game.black_won())

    def test_black_won_returns_correct_value(self):
        white = Player("Jan Kowalski", 1200)
        black = Player("Jan Nowak", 1200)

        game = Game(white, black, 2)

        self.assertTrue(game.black_won())
        self.assertFalse(game.white_won())