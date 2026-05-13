class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return self.__maxAreaBruteForce(heights) # Accepted
        return self.__maxAreaTwoPointer(heights)
    
    # TC - O(n^2) SC - O(1)
    def __maxAreaBruteForce(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)

        for i in range(n):
            for j in range(i + 1, n):
                height = min(heights[i], heights[j])
                breadth = j - i
                curr_area = height * breadth
                max_area = max(max_area, curr_area)
        
        return max_area
    
    # TC - O(n) SC - O(1)
    def __maxAreaTwoPointer(self, heights: List[int]) -> int:
        max_area = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            breadth = r - l
            curr_area = height * breadth
            max_area = max(max_area, curr_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area