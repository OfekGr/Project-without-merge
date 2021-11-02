from unittest import TestCase
from game_cards.Card import Card

class TestCard(TestCase):
    #If it receives more than 2 values
    def test_init_(self):
        Card.__init__(self, 4, 3, 4)

    #Test for value not in range
    def test_init2(self):
        Card.__init__(self, 1, 2)

    #test for suit not in range
    def test_init2(self):
        Card.__init__(self, 4, 5)

    # Check if card values are not integers
    def test_check_sign(self):
        Card.__init__(self, 'abcd', 3)

    #check valid and convert to string
    def test_check_sign2(self):
        Card.__init__(self, 2, 3)
        print(Card.check_sign(self))

    #Check highest possible values
    def test_check_sign3(self):
        Card.__init__(self, 14, 3)
        print(Card.check_sign(self))

    #Check value out of range
    def test_check_sign4(self):
        Card.__init__(self, 15, 3)
        print(Card.check_sign(self))

    #Check suit out of range
    def test_check_sign5(self):
        Card.__init__(self, 2, 4)
        print(Card.check_sign(self))


