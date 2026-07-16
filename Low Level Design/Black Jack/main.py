from game_round import GameRound
from user_player import UserPlayer
from dealer import Dealer
from deck import Deck
from hand import Hand

player = UserPlayer(Hand(), 1000)
dealer = Dealer(Hand())

while player.get_balance() > 0:
    GameRound(dealer, player, Deck()).play()