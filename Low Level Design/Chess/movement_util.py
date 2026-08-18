from piece import Piece
from square import Square
from color import Color

class MovementUtil:
    @staticmethod
    def is_valid_straight_move(start_row: int, start_col: int, end_row: int, end_col: int, color: Color, board: list[list[Square]]) -> bool:
        if not Piece.is_within_grid(start_row, start_col):
            return False

        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if ((row_movement != 0 and col_movement != 0)
            or (row_movement == 0 and col_movement == 0)):
            return False
        else:
            row_increment = 1 if end_row > start_row else -1
            col_increment = 1 if end_col > start_col else -1

            if row_movement == 0:
                y = start_col + col_increment
                while y != end_col:
                    if board[start_row][start_col].get_piece() is not None:
                        return False
                    y += col_increment
            else:
                x = start_row + row_increment
                while x != end_row:
                    if board[start_row][start_col].get_piece() is not None:
                        return False
                    x += row_increment

            if (board[end_row][end_col].get_piece() is not None 
                and board[end_row][end_col].get_piece().get_color() == color):
                return False

            return True

    @staticmethod
    def is_valid_diagonal_move(start_row: int, start_col: int, end_row: int, end_col: int, color: Color, board: list[list[Square]]) -> bool:
        if not Piece.is_within_grid(start_row, start_col):
            return False

        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement == 0 or col_movement == 0:
            return False

        if row_movement == col_movement:
            row_increment = 1 if end_row > start_row else -1
            col_increment = 1 if end_col > start_col else -1

            x = start_row + row_increment
            y = start_col + col_increment

            while x != end_row and y != end_col:
                if board[x][y].get_piece() is not None:
                    return False

                x += row_increment
                y += col_increment

            if (board[end_row][end_col].get_piece() is not None 
                and board[end_row][end_col].get_piece().get_color() == color):
                return False

            return True
        else:
            return False