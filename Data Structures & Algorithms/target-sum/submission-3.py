class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # return self.__recursive(0, nums, target, 0)
        return self.__topDown(nums, target)
    
    # TC - O(2 ^ N)
    # SC - O(N) -> Max depth of the Recursion Tree 
    def __recursive(self, i:int, nums: List[int], target: int, total_sum: int) -> int:
        if i == len(nums):
            return total_sum == target
        
        add = self.__recursive(i + 1, nums, target, total_sum + nums[i])
        subtract = self.__recursive(i + 1, nums, target, total_sum - nums[i])

        return add + subtract
    
    # TC - O(N * M)
    # SC - O(N * M + N) -> O(N * M) size of the memo array and O(N) is the recursion depth
    def __topDown(self, nums: List[int], target: int) -> int:
        N = len(nums)
        M = target
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