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
    def test_init3(self):
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

    #Check if the function gets the values correctly (different and same values)
    def test_check_sign6(self):
        c1=Card(2,3)
        c2=Card(3,2)
        c3=Card(8,1)
        c4=Card(9,0)
        c5=Card(12,3)
        c6=Card(12,3)
        self.assertNotEqual(Card.check_sign(c1), Card.check_sign(c2))
        self.assertNotEqual(Card.check_sign(c3), Card.check_sign(c1))
        self.assertNotEqual(Card.check_sign(c4), Card.check_sign(c5))
        self.assertEqual(Card.check_sign(c5), Card.check_sign(c6))


