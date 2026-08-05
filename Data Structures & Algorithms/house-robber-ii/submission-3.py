class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # return max(self.__rob_recursive(0, nums, True), self.__rob_recursive(1, nums, False))
        return self.__rob_top_down(nums)
        # return self.__rob_bottom_up(nums)
    
    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of nums
    def __rob_recursive(self, i: int, nums: List[int], flag: bool) -> int:
        if i >= len(nums):
            return 0
        
        if flag and i == len(nums) - 1:
            return 0
        
        take = nums[i] + self.__rob_recursive(i + 2, nums, flag or i == 0)

        skip = self.__rob_recursive(i + 1, nums, flag)

        return max(take, skip)

    # TC -> O(N)
    # SC -> O(N)
    def __rob_top_down(self, nums: List[int]) -> int:
        cache = [[-1] * 2 for _ in range(len(nums))]
        
        take_first_pos = self.__rob_top_down_helper(0, nums, 1, cache)
        skip_first_pos = self.__rob_top_down_helper(1, nums, 0, cache)
        return max(take_first_pos, skip_first_pos)

    def __rob_top_down_helper(self, i: int, nums: List[int], flag: int, cache: List[int]) -> int:
        if i >= len(nums):
            return 0

        if flag == 1 and i == len(nums) - 1:
            return 0
        
        if cache[i][flag] != -1:
            return cache[i][flag]

        take = nums[i] + self.__rob_top_down_helper(i + 2, nums, flag or (i == 0), cache)
        skip = self.__rob_top_down_helper(i + 1, nums, flag, cache)

        cache[i][flag] = max(take, skip)

        return cache[i][flag]

    def __rob_bottom_up_helper(self, nums: List[int]):
        take_first_pos = self.__rob_bottom_up_helper(nums[1:])
        skip_first_pos = self.__rob_bottom_up_helper(nums[:-1])
        
        return max(take_first_pos, skip_first_pos)
    
    def __rob_bottom_up_helper(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1] * 2 for _ in range(n)]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        

        return dp[n - 1]


