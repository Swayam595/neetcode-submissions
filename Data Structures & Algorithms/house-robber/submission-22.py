class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.__rob_recursive(0, nums)
        # return self.__rob_top_down(nums)
        return self.__rob_bottom_up(nums)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of the nums array
    def __rob_bottom_up(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            take = nums[i] + dp[i + 2]
            skip = dp[i + 1]
            dp[i] = max(take, skip)
        
        return dp[0]

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of the nums array
    def __rob_top_down(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        return self.__rob_top_down_helper(0, nums, memo)
    
    def __rob_top_down_helper(self, i: int, nums: List[int], memo: List[int]) -> int:
        if i >= len(nums):
            return 0
        
        if memo[i] != 0:
            return memo[i]
        
        take = nums[i] + self.__rob_top_down_helper(i + 2, nums, memo)
        skip = self.__rob_top_down_helper(i + 1, nums, memo)

        memo[i] = max(take, skip)
        return memo[i]


    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of the nums array
    def __rob_recursive(self, i: int, nums: List[int]) -> int:
        if i >= len(nums):
            return 0
        
        take = nums[i] + self.__rob_recursive(i + 2, nums)
        skip = self.__rob_recursive(i + 1, nums)
        
        return max(take, skip)