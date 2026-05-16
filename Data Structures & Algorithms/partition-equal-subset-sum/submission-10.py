class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not self.__isPossible(nums):
            return False

        # return self.__recursive(0, nums, 0, sum(nums) // 2)
        # return self.__topDown(nums)
        # return self.__bottomUp(nums)
        return self.__bottomUpOptimized(nums)
        
    # TC - O(N)
    # SC - O(1)
    def __isPossible(self, nums) -> bool:
        N = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        return True

    # TC - O(2 ^ N)
    # SC - O(N)
    def __recursive(self, i: int, nums: List[int], subset1_sum: int, target: int) -> bool:
        if target == 0:
            return True

        if i == len(nums) or target < 0:
            return  False
        
        take = self.__recursive(i + 1, nums, subset1_sum + nums[i], target - nums[i])
        skip = self.__recursive(i + 1, nums, subset1_sum, target)

        return take or skip

    # TC - O(N ^ 2)
    # SC - O(N + N * sum(nums) // 2)
    def __topDown(self, nums: List[int]) -> bool:
        N = len(nums)
        total_sum = sum(nums)
        target = total_sum // 2
        memo = [[-1] * (target + 1) for _ in range(N + 1)]
        return self.__topDownHelper(0, nums, memo, 0, target)
    
    # TC - O(N ^ 2)
    # SC - O(N)
    def __topDownHelper(self, i: int, nums: List[int], memo: List[List[int]], subset1_sum: int, target: int) -> int:
        if target == 0:
            return True
        
        if i == len(nums) or target < 0:
            return False
        
        if memo[i][target] != -1:
            return memo[i][target]
        
        take = self.__topDownHelper(i + 1, nums, memo, subset1_sum + nums[i], target - nums[i])
        skip = self.__topDownHelper(i + 1, nums, memo, subset1_sum, target)

        memo[i][target] = take | skip

        return memo[i][target]

    # TC - O(N ^ 2)
    # SC - O(N * sum(nums) // 2)
    def __bottomUp(self, nums: List[int]) -> bool:
        N = len(nums)
        total_sum = sum(nums)
        target = total_sum // 2
        dp = [[False] * (target + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = True

        for i in range(N - 1, -1, -1):
            for j in range(1, target + 1):
                take = dp[i + 1][j - nums[i]] if j - nums[i] >= 0 else False
                skip = dp[i + 1][j]
                dp[i][j] = take or skip
                
        return dp[0][target]

    # TC - O(N ^ 2)
    # SC - O(N * sum(nums) // 2)
    def __bottomUpOptimized(self, nums: List[int]) -> bool:
        N = len(nums)
        total_sum = sum(nums)
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(N - 1, -1, -1):
            new_dp = [False] * (target + 1)
            new_dp[0] = True
            for j in range(1, target + 1):
                take = dp[j - nums[i]] if j - nums[i] >= 0 else False
                skip = dp[j]

                new_dp[j] = take or skip
            dp = new_dp

        return dp[target]
