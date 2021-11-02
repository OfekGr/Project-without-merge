from game_cards.DeckOfCards import DeckOfCards
from game_cards.Player import Player
#Get 2 player names and the number of cards wanted per player (default is 26 cards),
# and set a variable to indicate that a game is off
class CardGame:
    def __init__(self, p1name = "player one", p2name = "player two", num_of_cards = 26):
        self.playerOne=Player(p1name, num_of_cards)
        self.playerTwo=Player(p2name, num_of_cards)
        self.deck = DeckOfCards()
        self.gameOn=False

#Make sure there is no game running, and if there isn't a game running, start a game, by shuffling the deck
    #  and giving the players cards up to the limit
    def new_game(self):
        if self.gameOn==False:
            self.gameOn=True
            self.deck.cards_shuffle()
            self.playerOne.set_hand(self.deck)
            self.playerTwo.set_hand(self.deck)
        else:
            raise AssertionError("Game already running")

#Compares the size of the decks between the players and declares the winner,
# in the case which both decks are equal, returns None
    def get_winner(self):
        if len(self.playerOne.playerhand) < len(self.playerTwo.playerhand):
            self.gameOn=False
            return f"game ended, {self.playerTwo.name} is the winner!"
        elif len(self.playerOne.playerhand) > len(self.playerTwo.playerhand):
            self.gameOn=False
            return f"game ended, {self.playerOne.name} is the winner!"
        elif len(self.playerOne.playerhand) == len(self.playerTwo.playerhand):
            self.gameOn=False
            return None
