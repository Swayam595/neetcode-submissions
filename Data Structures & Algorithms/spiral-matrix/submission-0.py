class Solution:
    # TC -> O(N * M)
    # SC -> O(1)
    # N -> # of rows
    # M -> # of columns
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        left = 0

        while left < right and top < bottom:
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
        
            for j in range(top, bottom):
                ans.append(matrix[j][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for k in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][k])
            bottom -= 1

            for l in range(bottom - 1, top - 1, -1):
                ans.append(matrix[l][left])
            left += 1
        
        return ans

