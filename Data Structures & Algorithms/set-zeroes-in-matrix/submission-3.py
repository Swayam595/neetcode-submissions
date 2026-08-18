class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        self.__brute_force(matrix)
        # self.__set_zeroes_inplace(matrix)

    # TC -> O((N * M))
    # SC -> O(1)
    def __set_zeroes_inplace(self, matrix: List[List[int]]) -> None:
        pass
    
    # TC -> O((N * M))
    # SC -> O(N + M)
    def __brute_force(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        rows = [False] * n
        cols = [False] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0