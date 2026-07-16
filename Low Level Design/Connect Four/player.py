from grid_position import GridPosition

class Player:
    def __init__(self, name: str, piece_color: GridPosition) -> None:
        self.__name = name
        self.__piece_color = piece_color
    
    def get_name(self) -> str:
        return self.__name
    
    def get_piece_color(self) -> GridPosition:
        return self.__piece_color