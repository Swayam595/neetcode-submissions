from piece import Piece
from color import Color
from square import Square

class Knight(Piece):
    def is_valid_move(self, start_row: int, start_col: int, end_row: int, end_col: int, board: list[list[Square]]) -> bool:
        if not Piece.is_within_grid(end_row, end_col):
            return False

        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if ((row_movement == 2 and col_movement == 1)
            or (row_movement == 1 and col_movement == 2)):
            if (board[end_row][end_col].get_piece() is not None
                and board[end_row][end_col].get_piece().get_color() == self.get_color()):
                return False

            return True

        return False

    def get_symbol(self):
        return "N" if self.get_color() == Color.WHITE else "n" 