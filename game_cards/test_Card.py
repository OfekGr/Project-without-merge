from unittest import TestCase
from game_cards.Card import Card

class TestCard(TestCase):
    #If it receives more than 2 values
    def test_init_(self):
        Card.__init__(self, 2, 3)

    # Check if card values are not integers
    def test_check_sign(self):
        Card.__init__(self, 2, 4)
        if type(self.value) != int or type(self.suit) != int:
            raise AssertionError("Card type is not a number")

