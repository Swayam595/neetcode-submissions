class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.__rob_recursive(0, nums)
        return self.__rob_top_down(nums)

    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of the nums
    def __rob_recursive(self, i: int, nums: List[int]) -> int:
        if i >= len(nums):
            return 0
        
        take = nums[i] + self.__rob_recursive(i + 2, nums)
        skip = self.__rob_recursive(i + 1, nums)

        return max(take, skip)

    # TC -> O(N ^ 2)
    # SC -> O(N)
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
