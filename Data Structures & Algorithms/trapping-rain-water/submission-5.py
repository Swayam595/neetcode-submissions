class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        # return self.__trap_brute_force(height)
        return self.__trap_prefix_suffix_array(height)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of height
    def __trap_prefix_suffix_array(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0
        prefix_max = [0] * n
        prefix_max[0] = height[0]

        suffix_max = [0] * n
        suffix_max[n - 1] = height[n - 1]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])

        for j in range(n - 2, -1, -1):
            suffix_max[j] = max(suffix_max[j + 1], height[j])

        for i in range(n):
            max_water = max_water + min(prefix_max[i], suffix_max[i]) - height[i]
        
        return max_water       

    
    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of height
    def __trap_brute_force(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)

        for i in range(n):
            left_max = height[i]
            right_max = height[i]

            for j in range(i):
                left_max = max(left_max, height[j])
            for k in range(i + 1, n):
                right_max = max(right_max, height[k])
            
            max_water = max_water + min(left_max, right_max) - height[i]

        return max_water