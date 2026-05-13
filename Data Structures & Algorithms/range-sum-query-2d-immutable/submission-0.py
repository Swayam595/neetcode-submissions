class NumMatrix:
    _prefix_cache = None

    def __init__(self, matrix: List[List[int]]):
        self._set_prefix_cache(matrix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r_o_d = self._prefix_cache[row2 + 1][col2 + 1]
        r_o_b = self._prefix_cache[row1][col2 + 1]
        r_o_c = self._prefix_cache[row2 + 1][col1]
        r_o_a = self._prefix_cache[row1][col1]

        return r_o_d - r_o_b - r_o_c + r_o_a

    def _set_prefix_cache(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        self._prefix_cache = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                self._prefix_cache[i+1][j+1] = (self._prefix_cache[i+1][j]
                                              + self._prefix_cache[i][j+1]
                                              + matrix[i][j]
                                              - self._prefix_cache[i][j])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)