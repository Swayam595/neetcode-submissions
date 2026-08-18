from abc import ABC, abstractmethod
from color import Color

class Piece(ABC):
    def __init__(self, color: Color):
        self.__color: Color = color

    def get_color(self):
        return self.__color

    @staticmethod
    def is_within_grid(end_row: int, end_col: int) -> bool:
        return 0 <= end_row < 8 and 0 <= end_col < 8

    @abstractmethod
    def is_valid_move(self, start_row: int, start_col: int, end_row: int, end_col: int, board) -> bool:
        pass

    @abstractmethod
    def get_symbol(self) -> str:
        pass