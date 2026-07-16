from card import Card

class Hand:
    def __init__(self) -> None:
        self.__score = 0
        self.__cards = []

    def add_card(self, card: Card) -> None:
        self.__cards.append(card)
        if card.get_value() == 1:
            self.__score += 11 if self.__score + 11 <= 21 else 1
        else:
            self.__score += card.get_value()
        print(f"Score: {self.__score}")
    
    def get_score(self) -> int:
        return self.__score

    def get_cards(self) -> list[Card]:
        return self.__cards
    
    def print(self) -> None:
        print ("Current Cards in hand: ")
        for card in self.__cards:
            print(card.print())