from player import Player
from hand import Hand

class Dealer(Player):
    def __init__(self, hand: Hand) -> None:
        super().__init__(hand)
        self.__target_score = 17

    def update_target_score(self, score: int) -> None:
        self.__target_score = score
    
    def make_move(self):
        return self.get_hand().get_score() < self.__target_score