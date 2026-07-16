from player import Player
from hand import Hand

class UserPlayer(Player):
    def __init__(self, hand: Hand, balance: int) -> None:
        super().__init__(hand)
        self.__balance = balance

    def get_balance(self) -> int:
        return self.__balance
    
    def place_bet(self, amount: int) -> int:
        if self.__balance < amount:
            raise ValueError("Insufficient Balance.")
        self.__balance -= amount
        return amount
    
    def recieve_winnings(self, amount: int) -> None:
        self.__balance += amount
    
    def make_move(self):
        if self.get_hand().get_score() > 21:
            return False
        move = input("Draw card? [y/n]: ")
        return move == 'y'