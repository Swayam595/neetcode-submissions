class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        self.__brute_force(matrix)
    
    # TC -> O((N * M) + (N + M))
    # SC -> O(N + M)
    def __brute_force(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        rows = set()
        cols = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for r in rows:
            for j in range(m):
                matrix[r][j] = 0
        
        for c in cols:
            for i in range(n):
                matrix[i][c] = 0