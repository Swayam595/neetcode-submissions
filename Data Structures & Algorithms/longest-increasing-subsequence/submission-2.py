class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.__recursive(0, nums, -float('inf'))
        return self.__top_down(nums)

    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of nums
    def __recursive(self, i: int, nums: List[int], prev: float) -> int:
        if i >= len(nums):
            return 0
        
        take = 0
        if prev < nums[i]:
            take = 1 + self.__recursive(i + 1, nums, nums[i])

        skip = self.__recursive(i + 1, nums, prev)

        return max(take, skip)

    def __top_down(self, nums: List[int]) -> int:
        memo = dict()

        return self.__top_down_helper(0, nums, -float('inf'), memo)

    def __top_down_helper(self, i: int, nums: List[int], prev: float, memo: dict) -> int:
        if i >= len(nums):
            return 0
        
        if (i, prev) in memo:
            return memo[(i, prev)]

        take = 0
        if prev < nums[i]:
            take = 1 + self.__top_down_helper(i + 1, nums, nums[i], memo)

        skip = self.__top_down_helper(i + 1, nums, prev, memo)

        memo[(i, prev)] = max(take, skip)
        return memo[(i, prev)]