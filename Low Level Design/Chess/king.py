from piece import Piece
from color import Color
from square import Square

class King(Piece):
    def is_valid_move(self, start_row: int, start_col: int, end_row: int, end_col: int, board: list[list[Square]]) -> bool:
        if not Piece.is_within_grid(start_row, start_col):
            return False

        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement > 1 or col_movement > 1:
            return False

        if (board[end_row][end_col].get_piece() is not None
            and board[end_row][end_col].get_piece().get_color() == self.get_color()):
            return False

        return True

    def get_symbol(self) -> str:
        return "K" if self.get_color() == Color.WHITE else "k"