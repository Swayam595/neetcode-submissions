class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWaterStored = 0

        while i < j:
            minHeightOfWater = min(heights[i], heights[j])
            waterWidth = j - i
            currMaxWaterStored = minHeightOfWater * waterWidth
            maxWaterStored = max(currMaxWaterStored, maxWaterStored)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxWaterStored