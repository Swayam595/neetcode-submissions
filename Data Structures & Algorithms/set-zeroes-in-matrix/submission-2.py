class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # self.__brute_force(matrix)
        self.__set_zeroes_inplace(matrix)

    # TC -> O((N * M))
    # SC -> O(1)
    def __set_zeroes_inplace(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row_zero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

    def print(self, matrix):
        for row in matrix:
            print (row)
        print ("\n")
    
    # TC -> O((N * M))
    # SC -> O(N + M)
    def __brute_force(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(ROWS):
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0