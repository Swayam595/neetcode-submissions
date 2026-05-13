class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.__robRecursively(nums, 0)   # Time limit exceeded 
        # return self.__robTopDown(nums, 0, [-1 for _ in range(len(nums))]) # Time limit exceeded 
        return self.__robBottomUp(nums)
    
    def __robRecursively(self, nums, i):
        if len(nums) <= i:
            return 0
        
        rob_ith_house = nums[i] + self.__robRecursively(nums, i + 2)
        leave_ith_house = self.__robRecursively(nums, i + 1)

        return max(rob_ith_house, leave_ith_house)
    
    def __robTopDown(self, nums, i, memo):
        if len(nums) <= i:
            return 0
        
        if memo[i] != -1:
            return memo[i]
        
        rob_ith_house = nums[i] + self.__robRecursively(nums, i + 2)
        leave_ith_house = self.__robRecursively(nums, i + 1)

        memo[i] = max(rob_ith_house, leave_ith_house)

        return memo[i]

    def __robBottomUp(self, nums):
        n = len(nums)
        
        if n <= 2:
            return max(nums)

        cache = [-1] * n
        cache[0] = nums[0]
        cache[1] = max(nums[1], cache[0])

        for i in range(2, n):
            rob_ith_house = nums[i] + cache[i - 2]
            leave_ith_house = cache[i - 1]
            cache[i] = max(rob_ith_house, leave_ith_house)
        
        return cache[n - 1]