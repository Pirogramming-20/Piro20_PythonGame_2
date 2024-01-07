from Player.Player import Player
from TimeGuessing import timeGuessingGame

player1 = Player("Yeonu", 5)
player2 = Player("Jimin", 5)
players = [player1, player2]
player1.setSelect(True)
player2.setSelect(False)
timeGuessingGame(players)