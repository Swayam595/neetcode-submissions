class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # self.__brute_force(matrix)
        self.__rotate_inplace(matrix)

    def __rotate_inplace(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        l = 0
        r = n - 1

        while l < r:
            for i in range(r - l):
                top = l
                bottom = r

                top_left = matrix[top][l + i]
                
                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = top_left

            r -= 1
            l += 1

    # TC -> O(N ^ 2)
    # SC -> O(N ^ 2)
    # N -> len of matrix
    def __brute_force(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        ans = []
        for j in range(n):
            column = []
            for i in range(n - 1, -1, -1):
                column.append(matrix[i][j])
            ans.append(column)

        for i in range(n):
            matrix[i] = ans[i]