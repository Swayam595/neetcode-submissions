class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        return self.__maxSubarraySumCircularBruteForce(nums)

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
                    