from grid_position import GridPosition
from player import Player
from grid import Grid

class Game:
    def __init__(self, grid: Grid, connect_n: int, target_score: int) -> None:
        self.__grid = grid
        self.__connect_n = connect_n
        self.__target_score = target_score

        self.__players = [
            Player("Player 1", GridPosition.RED),
            Player("Player 2", GridPosition.YELLOW)
        ]

        self.__score = {}

        for player in self.__players:
            self.__score[player.get_name()] = 0
    
    def print_board(self) -> None:
        print ('Board: \n')
        grid = self.__grid.get_grid()

        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GridPosition.EMPTY:
                    row += '0 '
                elif piece == GridPosition.RED:
                    row += 'R '
                else:
                    row += 'Y '
            print (row)
        print('')
    
    def play_move(self, player: Player) -> tuple:
        self.print_board()
        print (f"{player.get_name()}'s turn")
        column_count = self.__grid.get_column_count()
        print(column_count)
        move_column = int(input(f"Enter column between {0} and {column_count - 1} to add piece: "))
        move_row = self.__grid.place_disk(move_column, player.get_piece_color())
        return (move_row, move_column)

    def play_round(self) -> Player:
        while True:
            for player in self.__players:
                try:
                    row, col = self.play_move(player)
                    piece_color = player.get_piece_color()
                    if self.__grid.check_win(self.__connect_n, row, col, piece_color):
                        self.__score[player.get_name()] += 1
                        return player
                except ValueError as error:
                    print(f"Invalid Move: {error}")
    
    def play(self):
        max_score = 0
        winner = None

        while max_score < self.__target_score:
            winner = self.play_round()
            print (f"{winner.get_name()} won the round")
            max_score = max(self.__score[winner.get_name()], max_score)
            self.__grid.initGrid()
        
        print (f"{winner.get_name()} won the game")
