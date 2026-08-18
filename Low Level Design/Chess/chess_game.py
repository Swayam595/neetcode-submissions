from chess_board import ChessBoard
from player import Player
from color import Color

class ChessGame:
    def __init__(self):
        self.__board = ChessBoard()

        self.__white_player = Player(Color.WHITE)
        self.__black_player = Player(Color.BLACK)

        self.__current_player = self.__white_player

    def start_game(self):
        print("Welcome to Chess, UPPERCASE denotes white pieces, LOWERCASE denotes black pieces.")

        self.__board.display_board()

        current_player = self.__white_player

        while True:
            print("Current turn: ", str(current_player.get_color()))

            move_successful = self.__board.move_piece(self.__current_player)
            if move_successful:
                self.__board.display_board()
                self.__current_player = self.__black_player if self.__current_player == self.__white_player else self.__white_player
                current_player = self.__current_player
            else:
                print("Invalid move. Please try again")