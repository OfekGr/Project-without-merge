import random
from unittest import TestCase
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
class TestPlayer(TestCase):

    def setUp(self):
        pass

#Test if the player's hand is worth to the number of cards wanted per player
    def test_set_hand(self):
        Player.__init__(self, 'ofek')
        DeckOfCards.__init__(self)
        DeckOfCards.cards_shuffle(self)
        self.playerhand = self.cards[:26]
        Player.set_hand(self, self.playerhand)
        if len(self.playerhand) < self.NumOfCards:
            raise AssertionError("Player hand not maxed")
        elif len(self.playerhand) > self.NumOfCards:
            raise AssertionError("Player hand already full")

#Test if getting a card removes a card from the player's hand
    def test_get_card(self):
        Player.__init__(self, 'ofek')
        DeckOfCards.__init__(self)
        self.playerhand=self.cards
        Player.set_hand(self, self.playerhand)
        card_got=Player.get_card(self)
        if card_got in self.playerhand:
            raise AssertionError("card not removed from playerhand")

#Adding a random card to the deck (from 52 cards to 53 cards)
    def test_add_card(self):
        DeckOfCards.__init__(self)
        self.playerhand = self.cards
        DeckOfCards.__init__(self)
        Player.add_card(self, random.choice(self.cards))
        if len(self.playerhand) != len(self.cards)+1:
            raise AssertionError("card not added to playerhand")

    def tearDown(self):
        pass