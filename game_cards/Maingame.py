from game_cards.Card import Card
from game_cards.CardGame import CardGame
#Get 2 name inputs and number of cards per deck (default is 26, if higher than 26 or lower than 10, deck size is 26)
game=CardGame(input("Insert player1: "), input("Insert player2: "), int(input("insert amount of cards per player: ")))
game.new_game()
print("Player name: ", game.playerOne.name, "Player cards: ",game.playerOne.playerhand)
print("Player name: ", game.playerTwo.name, "Player cards: ",game.playerTwo.playerhand)

#10 rounds of gameplay, starting from 1 to 10, print out player names and players card and compare values
for i in range(1,11):
    print("round: ",i)
    p1card=game.playerOne.get_card()
    p2card=game.playerTwo.get_card()
    print({game.playerOne.name}, " card: ", {Card.check_sign(p1card)})
    print({game.playerTwo.name}, " card: ", {Card.check_sign(p2card)})
    winner=Card.__gt__(Card, p1card, p2card)
    #adds a card to the player who won the round
    if winner==True:
        game.playerOne.add_card(p2card)
        game.playerOne.add_card(p1card)
        print({game.playerOne.name}, "wins the round!")
    else:
        game.playerTwo.add_card(p2card)
        game.playerTwo.add_card(p1card)
        print({game.playerTwo.name}, "wins the round!")
print(game.playerOne.name, "has", len(game.playerOne.playerhand), "cards in hand.")
print(game.playerTwo.name, "has", len(game.playerTwo.playerhand), "cards in hand.")
#Compares deck sizes to decide who won the game
if len(game.playerOne.playerhand) == len(game.playerTwo.playerhand):
    print("Game ended, its a tie!")
else:
    print(game.get_winner())
