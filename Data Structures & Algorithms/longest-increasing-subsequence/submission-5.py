class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.__recursive(0, nums, -float('inf'))
        # return self.__top_down(nums)
        # return self.__bottom_up(nums)
        return self.__bottom_up_optimized(nums)

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

    # TC -> O(N ^ 2)
    # SC -> O(N ^ 2)
    # N -> len of nums
    def __top_down(self, nums: List[int]) -> int:
        memo = [[-1] * (len(nums) + 1) for _ in range(len(nums) + 1)]

        return self.__top_down_helper(0, nums, -1, memo)

    def __top_down_helper(self, i: int, nums: List[int], j: float, memo: List[List[int]]) -> int:
        if i >= len(nums):
            return 0
        
        if memo[i][j + 1] != -1:
            return memo[i][j + 1]

        take = 0
        if j == -1 or nums[j] < nums[i]:
            take = 1 + self.__top_down_helper(i + 1, nums, i, memo)

        skip = self.__top_down_helper(i + 1, nums, j, memo)

        memo[i][j + 1] = max(take, skip)
        return memo[i][j + 1]

    # TC -> O(N ^ 2)
    # SC -> O(N ^ 2)
    # N -> len of nums
    def __bottom_up(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                take = 0
                if j == -1 or nums[j] < nums[i]:
                    take = 1 + dp[i + 1][i + 1]
                skip = dp[i + 1][j + 1]
                dp[i][j + 1] = max(take, skip)

        return dp[0][0]

    # TC -> O(N ^ 2)
    # SC -> O(N)
    # N -> len of nums
    def __bottom_up_optimized(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            new_dp = [0] * (n + 1)
            for j in range(i - 1, -2, -1):
                take = 0
                if j == -1 or nums[j] < nums[i]:
                    take = 1 + dp[i + 1]
                skip = dp[j + 1]
                new_dp[j + 1] = max(take, skip)
            dp = new_dp
        
        return dp[0]