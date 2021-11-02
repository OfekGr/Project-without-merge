from game_cards.Card import Card
import random
#Define deck of cards, 13 numbers, and for each number, 4 values (shapes)
class DeckOfCards:
    def __init__(self):
        self.cards= []
        for v in range(2,15):
            for s in range(4):
                self.cards.append(Card(v,s))

#Shuffle the deck that was created in the list of self.cards
    def cards_shuffle(self):
        random.shuffle(self.cards)
        return self.cards

#Take one card out of the randomly generated deck, remove it and print it to the user
    def deal_one(self):
        test=random.choice(range(len(self.cards)))
        removed_card=self.cards[test]
        self.cards.pop(test)
        return removed_card

    def __str__(self):
        return f"cards deck: {self.cards}"

    def __repr__(self):
        return f"cards deck: {self.cards}"