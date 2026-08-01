class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.__rob_recursive(0, nums)
        # return self.__rob_top_down(nums)
        return self.__rob_bottom_up(nums)

    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of the nums
    def __rob_recursive(self, i: int, nums: List[int]) -> int:
        if i >= len(nums):
            return 0
        
        take = nums[i] + self.__rob_recursive(i + 2, nums)
        skip = self.__rob_recursive(i + 1, nums)

        return max(take, skip)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of the nums
    def __rob_top_down(self, nums: List[int]) -> int:
        N = len(nums)
        cache = [-1] * (N + 1)

        return self.__rob_top_down_helper(0, nums, cache)


    def __rob_top_down_helper(self, i: int, nums: List[int], cache:List[int]) -> int:
        if i >= len(nums):
            return 0

        if cache[i] != -1:
            return cache[i]

        take = nums[i] + self.__rob_top_down_helper(i + 2, nums, cache)
        skip = self.__rob_top_down_helper(i + 1, nums, cache)

        cache[i] = max(take, skip)

        return cache[i]

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def __rob_bottom_up(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 2)

        for i in range(N - 1, -1, -1):
            take = nums[i] + dp[i + 2]
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        
        return dp[0]
