class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return self.__maxAreaBruteForce(heights)
    
    # TC - O(n^2) SC - O(1)
    def __maxAreaBruteForce(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)

        for i in range(n):
            for j in range(i + 1, n):
                height = min(heights[i], heights[j])
                length = j - i
                curr_area = height * length
                max_area = max(max_area, curr_area)
        
        return max_area