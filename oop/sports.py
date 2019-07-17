from oop.exceptions import *

class Arena:
    def __init__(self):
        self.games = []
        self.standing = []

    def add_game(self, game):
        self.games.append(game)
        print(self.games)
        self._calc()

    def _calc(self):
        dct = {}
        for g in self.games:
            white = g.white
            black = g.black
            if not white in dct:
                dct[white] = 0
            if not black in dct:
                dct[black] = 0

            if g.white_won():
                dct[white] += 1
            else:
                dct[black] += 1

        print(dct)




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