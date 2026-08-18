from square import Square
from piece import Piece
from player import Player
from color import Color
from pawn import Pawn
from rook import Rook
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King

class ChessBoard:
    def __init__(self):
        self.__board: list[list[Square | None]] = [[None for _ in range(8)] for _ in range(8)]

        self.__initialize_board_and_pieces()

    def get_board(self) -> list[list[Square]]:
        return self.__board

    def move_piece(self, current_player: Player) -> bool:
        while True:
            start_row = int(input("Enter starting row: "))
            start_col = int(input("Enter starting col: "))

            end_row = int(input("Enter destination row: "))
            end_col = int(input("Enter destination col: "))

            if (not Piece.is_within_grid(end_row, end_col)
                or not Piece.is_within_grid(start_row, start_col)):
                return False

            piece_to_move: Piece = self.__board[start_row][start_col].get_piece()

            if not piece_to_move:
                print("There is no piece at the specified starting position.")
                continue

            if piece_to_move.get_color() != current_player.get_color():
                print("It is not your turn to move this piece")
                continue

            if piece_to_move.is_valid_move(start_row, start_col, end_row, end_col, self.__board):
                destination_piece = self.__board[end_row][end_col].get_piece()

                if destination_piece and destination_piece.get_color() != piece_to_move.get_color():
                    self.__board[end_row][end_col].set_piece(None)

                self.__board[end_row][end_col].set_piece(piece_to_move)
                self.__board[start_row][start_col].set_piece(None)

                print(f"{piece_to_move.get_symbol()} moved to {end_row}, {end_col}")
                return True
            else:
                print(f"Invalid move for the {piece_to_move.get_symbol()}. Please try again.")

    def display_board(self) -> None:
        print("  0 1 2 3 4 5 6 7")
        print("  ---------------")
        for i in range(8):
            print(i, end = "|")
            for j in range(8):
                piece = self.__board[i][j].get_piece()
                print(piece.get_symbol() + " " if piece else ". ", end = "")
            print()

    def __initialize_board_and_pieces(self) -> None:
        for i in range(8):
            for j in range(8):
                square_color = Color.BLACK if (i + j) % 2 == 0 else Color.WHITE
                self.__board[i][j] = Square(square_color)


        self.__initialize_black_pieces()
        self.__initialize_white_pieces()

    def __initialize_black_pieces(self) -> None:
        for i in range(8):
            self.__board[1][i].set_piece(Pawn(Color.BLACK))

        self.__board[0][0].set_piece(Rook(Color.BLACK))
        self.__board[0][7].set_piece(Rook(Color.BLACK))

        self.__board[0][1].set_piece(Knight(Color.BLACK))
        self.__board[0][6].set_piece(Knight(Color.BLACK))

        self.__board[0][2].set_piece(Bishop(Color.BLACK))
        self.__board[0][5].set_piece(Bishop(Color.BLACK))

        self.__board[0][3].set_piece(Queen(Color.BLACK))

        self.__board[0][4].set_piece(King(Color.BLACK))

    def __initialize_white_pieces(self) -> None:
        for i in range(8):
            self.__board[6][i].set_piece(Pawn(Color.WHITE))

        self.__board[7][0].set_piece(Rook(Color.WHITE))
        self.__board[7][7].set_piece(Rook(Color.WHITE))

        self.__board[7][1].set_piece(Knight(Color.WHITE))
        self.__board[7][6].set_piece(Knight(Color.WHITE))

        self.__board[7][2].set_piece(Bishop(Color.WHITE))
        self.__board[7][5].set_piece(Bishop(Color.WHITE))

        self.__board[7][3].set_piece(Queen(Color.WHITE))

        self.__board[7][4].set_piece(King(Color.WHITE))
