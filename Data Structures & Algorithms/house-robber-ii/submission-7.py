class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # return max(
        #     self.__rob_recursive(0, nums, True),
        #     self.__rob_recursive(1, nums, False)
        # )
        return self.__rob_top_down(nums)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of the nums array
    def __rob_top_down(self, nums: List[int]) -> int:
        memo = [[-1] * 2 for _ in range(len(nums) + 1)]
        return max(
            self.__rob_top_down_helper(0, nums, memo, 1),
            self.__rob_top_down_helper(1, nums, memo, 0)
        )


    def __rob_top_down_helper(self, i: int, nums: List[int], memo: List[int], flag: bool) -> int:
        if i >= len(nums):
            return 0
        
        if flag and i == len(nums) - 1:
            return 0
        
        if memo[i][flag] != -1:
            return memo[i][flag]

        take = nums[i] + self.__rob_top_down_helper(i + 2, nums, memo, flag or i == 0)
        skip = self.__rob_top_down_helper(i + 1, nums, memo, flag)

        memo[i][flag] = max(take, skip)
        return memo[i][flag]


    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of nums
    def __rob_recursive(self, i: int, nums: List[int], flag:  bool) -> int:
        if i >= len(nums):
            return 0
        
        if flag and i == len(nums) - 1:
            return 0
        
        take = nums[i] + self.__rob_recursive(i + 2, nums, flag or i == 0)
        skip = self.__rob_recursive(i + 1, nums, flag)

        return max(take, skip)