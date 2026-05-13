class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return self.__bruteForce(nums) # Accepted
        return self.__kadanes(nums) # Accepted

    # TC - O(n^2) SC - O(1)
    def __bruteForce(self, nums: List[int]) -> int:
        max_sum = -float('inf')

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
    # TC - O(n) SC - O(1)
    def __kadanes(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum