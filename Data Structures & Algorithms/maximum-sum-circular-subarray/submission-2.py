class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # return self.__maxSubarraySumCircularBruteForce(nums) # Accepted
        return self.__prefixSuffixSum(nums)

    # TC - O(n^2) SC - O(1)
    def __maxSubarraySumCircularBruteForce(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, i + n):
                curr_sum += nums[j % n]
            
                max_sum = max(max_sum, curr_sum)
        return max_sum
    
    def __prefixSuffixSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        suffix_sum = [0] * n
        suffix_max_sum = nums[n - 1]

        suffix_sum[n - 1] = nums[n - 1]

        max_sum = -float('inf')

        
        for i in range(n - 2, -1, -1):
            suffix_max_sum += nums[i]
            suffix_sum[i] = max(suffix_sum[i + 1] , suffix_max_sum)

        curr_max = 0
        prefix_sum = 0
        
        for j in range(n):
            curr_max += nums[j]
            max_sum = max(max_sum, curr_max)

            if curr_max < 0:
                curr_max = 0

            prefix_sum += nums[j]

            if j + 1 < n:
                max_sum = max(max_sum, prefix_sum + suffix_sum[j + 1])

            
        
        return max_sum

                    