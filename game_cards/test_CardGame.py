import random
from unittest import TestCase
from game_cards.CardGame import CardGame
from game_cards.Player import Player

class TestCardGame(TestCase):

#Test without giving names
    def test_no_name(self):
        CardGame.__init__(self)
        print(self.playerOne.name)
        print(self.playerTwo.name)

#Test if players got different hands
    def test_new_game(self):
        CardGame.__init__(self, 'ofek', 'bob')
        self.playerOne.set_hand(self.deck)
        p1hand=self.playerOne.playerhand
        self.playerTwo.set_hand(self.deck)
        p2hand=self.playerTwo.playerhand
        if p1hand==p2hand:
            raise AssertionError("Cards are the same")

#Try running the game again while the 1st is still going
    def test_new_game1(self):
        CardGame.__init__(self, 'ofek', 'bob')
        CardGame.new_game(self)
        CardGame.new_game(self)

#Testing if the function returns None if both playerhands have the same amount of cards
    def test_get_winner(self):
        CardGame.__init__(self, 'ofek', 'bob')
        self.playerOne.playerhand=self.playerTwo.playerhand
        if CardGame.get_winner(self) == None:
            print("Its a tie!")

#Testing if player one has a larger deck
    def test_get_winner2(self):
        CardGame.__init__(self)
        CardGame.new_game(self)
        self.playerOne.playerhand
        (self.playerTwo.playerhand).pop()
        print(CardGame.get_winner(self))

#Testing if player two has a larger deck
    def test_get_winner3(self):
        CardGame.__init__(self)
        CardGame.new_game(self)
        (self.playerOne.playerhand).pop()
        self.playerTwo.playerhand
        print(CardGame.get_winner(self))


