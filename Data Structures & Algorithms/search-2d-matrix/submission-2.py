class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        h = (n * m) - 1

        while l <= h:
            mid = l + (h - l) // 2
            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return False