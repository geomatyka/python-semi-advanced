from oop.exceptions import *

class Arena:
    def __init__(self):
        self.games = []
        self._standing = []

    def add_game(self, game):
        self.games.append(game)
        # print(self.games)
        self._calc()

    def _calc(self):
        wins = {}
        for g in self.games:
            white = g.white
            black = g.black
            if not white in wins:
                wins[white] = 0
            if not black in wins:
                wins[black] = 0

            if g.white_won():
                wins[white] += 1
            else:
                wins[black] += 1

        # print(wins)
        self._standing = [player for player, n in sorted(wins.items(), key=lambda x: x[1], reverse=True)]

    def standing(self):
        return self._standing



class Player:
    def __init__(self, name, ranking):
        if len(name) < 3:
            raise NameTooShortException
        self.name = name
        self.ranking = ranking

    def description(self):
        return f"My name is {self.name} and my ranking is {self.ranking}."


class Game:
    def __init__(self, white, black, winner):
        self.white = white
        self.black = black
        self.winner = winner

        if self.winner not in (1,2):
            raise WrongWinnerException

    def white_won(self):
        if self.winner == 1:
            return True
        return False

    def black_won(self):
        return self.winner == 2