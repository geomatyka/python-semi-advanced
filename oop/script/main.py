from oop.sports import *


def print_lower_case(string):
    print(string.lower())


def print_upper_case(string):
    print(string.upper())


def print_first_letter(string):
    print(string[0])

def print_modified_string(string, modifier):
    print(modifier(string))

def to_lower_case(string):
    return string.lower()


if __name__ == '__main__':
    player = Player('aaa',1)
    player1 = Player("Jan Kowalski", 1200)
    player2 = Player("Jan Nowak", 1200)
    player3 = Player("Jan Kowalski", 1200)
    game1 = Game(player1, player2, 1)
    game2 = Game(player1, player3, 2)
    game3 = Game(player2, player3, 2)

    print(player1.__hash__())
    print(player1 == 1)

    print_modified_string("Hello World!", lambda x: x+x)
    print_modified_string("Hello World!", to_lower_case)

    # hello = "Hello World!"
    # print(map(lambda x: x.lower, hello))