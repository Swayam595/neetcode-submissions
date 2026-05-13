class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        return self.__pivotIndexBruteForce(nums)
    
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