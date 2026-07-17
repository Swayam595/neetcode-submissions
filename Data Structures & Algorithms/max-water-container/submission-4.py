class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            max_water = max(max_water, height * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water