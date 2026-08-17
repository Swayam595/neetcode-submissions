class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.__brute_force(matrix)

    # TC -> O(N ^ 2)
    # SC -> O(N ^ 2)
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