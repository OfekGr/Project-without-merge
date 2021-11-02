import random
from unittest import TestCase
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
class TestPlayer(TestCase):

    def setUp(self):
        pass

    # Test if the number of cards to deal per player is less than 10
    def test_set_hand1(self):
        Player.__init__(self, 'ofek', 9)
        if self.NumOfCards != 26:
            raise AssertionError("didn't give default number of cards in hand (26)")

    # Test if the number of cards to deal per player is more than 26
    def test_set_hand2(self):
        Player.__init__(self, 'ofek', 27)
        if self.NumOfCards != 26:
            raise AssertionError("didn't give default number of cards in hand (26)")

    # Test if the number of cards to deal per player is equal to number put
    def test_set_hand2(self):
        Player.__init__(self, 'ofek', 25)
        if self.NumOfCards != 25:
            raise AssertionError("didn't give the player the wanted number of cards")


# Test if the player's hand is worth to the number of cards wanted per player
    def test_set_hand(self):
        Player.__init__(self, 'ofek')
        DeckOfCards.__init__(self)
        DeckOfCards.cards_shuffle(self)
        cut_deck=int((len(self.cards))/2)
        self.playerhand = self.cards[:cut_deck]
        Player.set_hand(self, self.playerhand)
        if len(self.playerhand) < self.NumOfCards:
            raise AssertionError("Player hand not maxed")
        elif len(self.playerhand) > self.NumOfCards:
            raise AssertionError("Player hand already full")

# Test if getting a card removes a card from the player's hand
    def test_get_card(self):
        Player.__init__(self, 'ofek')
        DeckOfCards.__init__(self)
        self.playerhand=self.cards
        Player.set_hand(self, self.playerhand)
        card_got=Player.get_card(self)
        if card_got in self.playerhand:
            raise AssertionError("card not removed from playerhand")

# Adding a random card to the deck (from 52 cards to 53 cards)
    def test_add_card(self):
        DeckOfCards.__init__(self)
        self.playerhand = self.cards
        DeckOfCards.__init__(self)
        Player.add_card(self, random.choice(self.cards))
        if len(self.playerhand) != len(self.cards)+1:
            raise AssertionError("card not added to playerhand")

    def tearDown(self):
        pass