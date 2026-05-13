class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # return self.__pivotIndexBruteForce(nums) # Accepted but inefficient TC is O(n^2)
        # return self.__pivotIndexPrefixSum(nums) # Accepted and efficient TC is O(n)
        return self.__pivotIndexPrefixSumOptimal(nums) # Accepted and more efficient TC is O(n) and SC is O(1)
    
    # TC - O(n^2) SC - O(1)
    def __pivotIndexBruteForce(self, nums: List[int]) -> int:
        prefix_sum = 0

        n = len(nums)

        for i in range(n):
            postfix_sum = 0
            for j in range(i + 1, n):
                postfix_sum += nums[j]
            if prefix_sum == postfix_sum:
                return i
            prefix_sum += nums[i]
        
        return -1
    
    # TC - O(n) SC - O(n)
    def __pivotIndexPrefixSum(self, nums: List[int]) -> int:
        n = len(nums)
        postfix_sum = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            postfix_sum[i] = postfix_sum[i + 1] + nums[i]

        prefix_sum = 0

        for j in range(n):
            if prefix_sum == postfix_sum[j + 1]:
                return j
            prefix_sum += nums[j]
        
        return -1
    
    # TC - O(n) SC - O(1)
    def __pivotIndexPrefixSumOptimal(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1