class Solution:
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # TC - O(N * M)
    # SC - O(N * M)
    # N is the number of rows in the grid.
    # M is the number of columns in the grid
    def numIslands(self, grid: List[List[str]]) -> int:
        self.__N = len(grid)
        self.__M = len(grid[0])
        self.__visited = set()
        count = 0
        for i in range(self.__N):
            for j in range(self.__M):
                if self.__exploreIfIsland(i, j, grid):
                    count += 1
        
        return count

    def __exploreIfIsland(self, x: int, y: int, grid: List[List[str]]) -> bool:
        if not self.__canExplore(x, y, grid):
            return False

        self.__visited.add((x, y))
        
        for x_offset, y_offset in self.DIRECTIONS:
            x_new = x + x_offset
            y_new = y + y_offset

            self.__exploreIfIsland(x_new, y_new, grid)
        
        return True
        
    def __canExplore(self, x: int, y: int, grid: List[List[str]]) -> bool:
        return self.__isValidCordinate(x, y) and self.__isNotVisited(x, y) and self.__isIslad(x, y, grid)

    def __isValidCordinate(self, x: int, y: int) -> bool:
        return 0 <= x < self.__N and 0 <= y < self.__M

    def __isNotVisited(self, x: int, y: int) -> bool:
        return not ((x, y) in self.__visited)
    
    def __isIslad(self, x: int, y: int, grid: List[List[str]]) -> bool:
        return grid[x][y] == "1"