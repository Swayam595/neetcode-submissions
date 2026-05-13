class Solution:
    def trap(self, heights: List[int]) -> int:
        # return self.__trapBruteForce(heights) # Accepted
        # return self.__trapPrefixSuffix(heights) # Accepted
        return self.__trapTwoPointers(heights) # Accepted

    
    # TC - O(n^2) SC - O(1)
    def __trapBruteForce(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        
        n = len(heights)
        ans = 0

        for i in range(n):
            left_max = heights[i]
            right_max = heights[i]

            for j in range(i):
                left_max = max(left_max, heights[j])
            
            for k in range(i + 1, n):
                right_max = max(right_max, heights[k])
            
            ans += min(left_max, right_max) - heights[i]
        
        return ans
    
    # TC - O(n) SC - O(n)
    def __trapPrefixSuffix(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        
        ans = 0
        n = len(heights)

        prefix_max = [0] * n
        suffix_max = [0] * n

        prefix_max[0] = heights[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], heights[i])
        
        suffix_max[n - 1]= heights[n - 1]

        for j in range(n - 2, -1, -1):
            suffix_max[j] = max(suffix_max[j + 1], heights[j])

        for k in range(n):
            ans += min(prefix_max[k], suffix_max[k]) - heights[k]
        
        return ans
    
    # TC - O(n) SC - O(1)
    def __trapTwoPointers(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        
        ans = 0
        l = 0
        r = len(heights) - 1

        left_max = heights[l]
        right_max = heights[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, heights[l])
                ans += left_max - heights[l]
            else:
                r -= 1
                right_max = max(right_max, heights[r])
                ans += right_max - heights[r]
        
        return ans