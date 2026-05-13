class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # return self.__recursive(0, nums, target, 0)
        # return self.__topDown(nums, target)
        # return self.__bottopUp(nums, target)
        return self.__bottopUpOptimized(nums, target)
    
    # TC - O(2 ^ N)
    # SC - O(N) -> Max depth of the Recursion Tree 
    def __recursive(self, i:int, nums: List[int], target: int, total_sum: int) -> int:
        if i == len(nums):
            return total_sum == target
        
        add = self.__recursive(i + 1, nums, target, total_sum + nums[i])
        subtract = self.__recursive(i + 1, nums, target, total_sum - nums[i])

        return add + subtract
    
    # TC - O(N * M)
    # SC - O(N * M + N) where O(N * M) size of the memo array and O(N) is the recursion depth
    # N - Len(nums)
    # M - Total sum of the array
    def __topDown(self, nums: List[int], target: int) -> int:
        N = len(nums)
        total_sum = sum(nums)
        memo = [[None] * (2 * total_sum + 1) for _ in range(N + 1)]
        
        return self.__topDownHelper(0, nums, target, memo, 0, total_sum)

    def __topDownHelper(self, i: int, nums: List[int], target: int, memo: List[List[None | int]], curr_sum: int, total_sum: int) -> int:
        if i == len(nums):
            return curr_sum == target

        if memo[i][total_sum + curr_sum] != None:
            return memo[i][total_sum + curr_sum]
        
        add = self.__topDownHelper(i + 1, nums, target, memo, curr_sum + nums[i], total_sum)
        subtract = self.__topDownHelper(i + 1, nums, target, memo, curr_sum - nums[i], total_sum)

        memo[i][total_sum + curr_sum] = add + subtract
        
        return memo[i][total_sum + curr_sum]

    # TC - O(N * M)
    # SC - O(N * M) where O(N * M) size of the dp array
    # N - Len(nums)
    # M - Total sum of the array
    def __bottopUp(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]

    # TC - O(N * M)
    # SC - O(M) where 
    # M - Total sum of the array
    def __bottopUpOptimized(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp
        
        return dp[target]