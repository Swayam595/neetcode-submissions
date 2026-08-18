from color import Color

class Player:
    def __init__(self, color: Color):
        self.__color = color

    def get_color(self) -> Color:
        return self.__color