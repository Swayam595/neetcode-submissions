class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return self.__recursive(0, nums, 0, 0)
        return self.__topDown(nums)

    # TC - O(2 ^ N)
    # SC - O(N)
    def __recursive(self, i: int, nums: List[int], subset1_sum: int, subset2_sum: int) -> bool:
        if i == len(nums):
            return  subset1_sum == subset2_sum
        
        take = self.__recursive(i + 1, nums, subset1_sum + nums[i], subset2_sum)
        skip = self.__recursive(i + 1, nums, subset1_sum, subset2_sum + nums[i])

        return take or skip

    def __topDown(self, nums: List[int]) -> bool:
        N = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        memo = [[-1] * (target + 1) for _ in range(N + 1)]
        return self.__topDownHelper(0, nums, memo, 0, target) != 0
    
    def __topDownHelper(self, i: int, nums: List[int], memo: List[List[int]], subset1_sum: int, target: int) -> int:
        if target == 0:
            return True
        
        if i == len(nums) or target < 0:
            return False
        
        if memo[i][target] != -1:
            return memo[i][target]
        
        take = self.__topDownHelper(i + 1, nums, memo, subset1_sum + nums[i], target - nums[i])
        skip = self.__topDownHelper(i + 1, nums, memo, subset1_sum, target)

        memo[i][target] = take or skip

        return memo[i][target]