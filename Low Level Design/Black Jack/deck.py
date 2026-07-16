import random

from suite import Suite
from card import Card

class Deck:
    def __init__(self) -> None:
        self.__cards = []
        self.__init_deck()
    
    def print(self) -> None:
        for card in self.__cards:
            print(card.print())
        
    def draw(self) -> Card:
        return self.__cards.pop()
    
    def suffle(self) -> None:
        for i in range(len(self.__cards)):
            j = random.randint(0, i)
            self.__cards[j], self.__cards[i] = self.__cards[i], self.__cards[j]

    def __init_deck(self) -> None:
        for suite in Suite:
            for value in range(1, 14):
                card_value = min(value, 10)
                self.__cards.append(Card(suite, card_value))
