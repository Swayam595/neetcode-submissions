class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.__rob_recursive(0, nums)
        return self.__rob_top_down(nums)

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