class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # self.__brute_force(matrix)
        self.__rotate_inplace(matrix)

    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of matrix
    def __rotate_inplace(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        l = 0
        r = n - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

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