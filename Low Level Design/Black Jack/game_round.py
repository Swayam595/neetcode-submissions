from player import Player
from deck import Deck

class GameRound:
    def __init__(self, dealer: Player, player: Player, deck: Deck) -> None:
        self.__dealer = dealer
        self.__player = player
        self.__deck = deck
    
    def get_bet_user(self) -> int:
        amount = int(input("Ebter a bet amount: "))
        return amount

    def deal_initial_cards(self) -> None:
        for _ in range(2):
            self.__dealer.add_card(self.__deck.draw())
            self.__player.add_card(self.__deck.draw())
        
        print ("Player Hand: ")
        self.__player.get_hand().print()

        dealer_card = self.__dealer.get_hand().get_cards()[0]
        print("Dealer's first card: ")
        dealer_card.print()
    
    def cleanup_round(self) -> None:
        self.__player.clear_hand()
        self.__dealer.clear_hand()
        print(f"Player's balance: {self.__player.get_balance()}")

    def play(self) -> None:
        self.__deck.suffle()

        if self.__player.get_balance() <= 0:
            print("Insufficient Balance.")
            return
        
        user_bet = self.get_bet_user()
        self.__player.place_bet(user_bet)

        while self.__player.make_move():
            draw_card = self.__deck.draw()
            print(f"Player Draws: {draw_card.print()}")

            self.__player.add_card(draw_card)
            print(f"Player Score: {self.__player.get_hand().get_score()}")

        if self.__player.get_hand().get_score() > 21:
            print("Dealer Wins")
            self.cleanup_round()
            return
        
        while self.__dealer.make_move():
            draw_card = self.__deck.draw()
            self.__dealer.add_card(draw_card)

        dealers_score = self.__dealer.get_hand().get_score()
        players_score = self.__player.get_hand().get_score()

        if dealers_score > 21 or players_score > dealers_score:
            print("Player own the round.")
            self.__player.recieve_winnings(user_bet * 2)
        elif players_score < dealers_score:
            print("Dealer Won the round")
        else:
            print("Round Draw")
            self.__player.recieve_winnings(user_bet)
        
        self.cleanup_round()
