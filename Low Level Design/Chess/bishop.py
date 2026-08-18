from movement_util import MovementUtil
from piece import Piece
from color import Color
from square import Square

class Bishop(Piece):
    def is_valid_move(self, start_row: int, start_col: int, end_row: int, end_col: int, board: list[list[Square]]) -> bool:
        return MovementUtil.is_valid_diagonal_move(start_row, start_col, end_row, end_col, self.get_color(), board)

    def get_symbol(self) -> str:
        return "B" if self.get_color() == Color.WHITE else "b"