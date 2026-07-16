from abc import ABC, abstractmethod
from hand import Hand
from card import Card

class Player(ABC):
    def __init__(self, hand: Hand) -> None:
        self.__hand = hand
    
    def get_hand(self) -> Hand:
        return self.__hand
    
    def clear_hand(self) -> None:
        self.__hand = Hand()

    def add_card(self, card: Card) -> None:
        self.__hand.add_card(card)
    
    @abstractmethod
    def make_move(self):
        pass
