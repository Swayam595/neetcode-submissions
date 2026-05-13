class Solution:
    def trap(self, heights: List[int]) -> int:
        return self.__trapBruteForce(heights) # 
    
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