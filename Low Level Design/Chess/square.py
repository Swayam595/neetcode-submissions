from color import Color
from piece import Piece

class Square:
    def __init__(self, color: Color):
        self.__color: Color = color
        self.__piece: Piece = None

    def get_color(self) -> Color:
        return self.__color

    def get_piece(self) -> Piece:
        return self.__piece

    def set_piece(self, piece: Piece) -> None:
        self.__piece = piece