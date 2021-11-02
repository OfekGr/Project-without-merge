import random
#Define player name and deck size
class Player:
    def __init__(self, name, NumOfCards = 26):
        self.name = name
        self.NumOfCards = NumOfCards
        self.playerhand = []
        if NumOfCards > 26 or NumOfCards < 10:
            self.NumOfCards=26

#Giving player cards up to the card limit (NumOfCards)
    def set_hand(self, cards):
        for i in range(self.NumOfCards):
            if (len(self.playerhand) < (self.NumOfCards)):
                self.playerhand.append(cards.deal_one())

#Play a card from the player's hand and remove it from the hand
    def get_card(self):
        card_index=random.choice(range(len(self.playerhand)))
        return self.playerhand.pop(card_index)

#Get a card and add it to the player's hand
    def add_card(self, card):
        self.playerhand.append(card)

    def __str__(self):
        return 'Playerhand:', {self.playerhand}, 'number of cards in hand:', {self.NumOfCards}

    def __repr__(self):
        return 'Playerhand:', {self.playerhand}, 'number of cards in hand:', {self.NumOfCards}

