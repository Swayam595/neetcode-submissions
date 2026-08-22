class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return self.__max_area_bruteForce(heights)
        return self.__max_area_2_pointers(heights)

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of heights array
    def __max_area_2_pointers(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_water = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            max_water = max(max_water, width * height)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_water 

    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of heights array
    def __max_area_bruteForce(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)

        for l in range(n):
            for r in range(l + 1, n):
                height = min(heights[l], heights[r])
                width = r - l
                max_water = max(max_water, height * width)
        
        return max_water