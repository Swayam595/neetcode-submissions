from piece import Piece
from color import Color
from square import Square

class Pawn(Piece):
    def is_valid_move(self, start_row: int, start_col: int, end_row: int, end_col: int, board: list[list[Square]]) -> bool:
        if not Piece.is_within_grid(end_row, end_col):
            return False

        row_movement = end_row - start_row
        col_movement = end_col - start_col

        direction = -1 if self.get_color() == Color.WHITE else 1

        if col_movement != 0:
            return False

        if row_movement == direction and board[end_row][end_col].get_piece() is None:
            return True

        if (self.is_first_move(start_row) 
            and row_movement == (2 * direction) 
            and board[start_row + direction][start_col].get_piece() is None
            and board[end_row][end_col].get_piece() is None):
            return True

        return False

    def get_symbol(self):
        return "P" if self.get_color() == Color.WHITE else "p"

    def is_first_move(self, start_row: int) -> bool:
        return (
            (self.get_color() == Color.WHITE and start_row == 6)
            or (self.get_color() == Color.BLACK and start_row == 1)
        )

    