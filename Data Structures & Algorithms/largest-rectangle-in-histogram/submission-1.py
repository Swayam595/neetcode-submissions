class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # return self.__largest_rectangle_area_brute_force(heights)
        return self.__largest_rectangle_area_stack(heights)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of heights
    def __largest_rectangle_area_stack(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        stack = []
        left_most = [-1] * n
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if len(stack) > 0:
                left_most[i] = stack[-1]
            stack.append(i)

        stack = []
        right_most = [n] * n
        for j in range(n - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[j]:
                stack.pop()
            
            if len(stack) > 0:
                right_most[j] = stack[-1]
            stack.append(j)
        
        for k in range(n):
            left_most[k] += 1
            right_most[k] -= 1
            max_area = max(max_area, heights[k] * (right_most[k] - left_most[k] + 1))
        
        return max_area

    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of heights
    def __largest_rectangle_area_brute_force(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            curr_height = heights[i]

            right_most = i + 1
            while right_most < n and heights[right_most] >= curr_height:
                right_most += 1
            
            left_most = i - 1
            while left_most >= 0 and heights[left_most] >= curr_height:
                left_most -= 1
            
            right_most -= 1
            left_most += 1
            max_area = max(max_area, curr_height * (right_most - left_most + 1))
        
        return max_area