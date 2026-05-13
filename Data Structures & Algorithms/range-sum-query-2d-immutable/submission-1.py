class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.__set_prefix_caache(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r_o_d = self.__cache[row2 + 1][col2 + 1]
        r_o_a = self.__cache[row1][col1]
        r_o_b = self.__cache[row1][col2 + 1]
        r_o_c = self.__cache[row2 + 1][col1]

        return r_o_d - r_o_b - r_o_c + r_o_a

    def __set_prefix_caache(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        self.__cache = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.__cache[i + 1][j +1 ] = (self.__cache[i + 1][j]
                                        + self.__cache[i][j + 1]
                                        + matrix[i][j] 
                                        - self.__cache[i][j])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)