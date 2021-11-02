from unittest import TestCase
from game_cards.DeckOfCards import DeckOfCards



class TestDeckOfCards(TestCase):

    def setUp(self):
        pass

#Test if it actually shuffles randomly
    def test_cards_shuffle(self):
        DeckOfCards.__init__(self)
        deck1=DeckOfCards.cards_shuffle(self)
        DeckOfCards.__init__(self)
        deck2=DeckOfCards.cards_shuffle(self)
        if deck1 == deck2:
            raise AssertionError("Deck did not shuffle")



#Test if after getting one card, it is actually removed from the deck
    def test_deal_one(self):
        DeckOfCards.__init__(self)
        card1=DeckOfCards.deal_one(self)
        if len(self.cards) == 52:
            raise AssertionError("card not removed")
        if card1 in self.cards:
            print("Card in deck")
        else:
            print("Card not in deck")

    def tearDown(self):
        pass
