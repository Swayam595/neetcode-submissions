class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return self.__brute_force(nums)
        return self.__kadnes_algo(nums)

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of nums
    def __kadnes_algo(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        curr_sum = 0

        n = len(nums)

        for i in range(n):
            curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0
            
        
        return max_sum
    
    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of nums
    def __brute_force(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum 