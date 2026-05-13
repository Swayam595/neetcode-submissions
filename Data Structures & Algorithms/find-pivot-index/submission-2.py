class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # return self.__pivotIndexBruteForce(nums) # Accepted
        return self.__pivotIndexPrefixSum(nums) #
    
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
    
    def __pivotIndexPrefixSum(self, nums: List[int]) -> int:
        n = len(nums)
        postfix_sum = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            postfix_sum[i] = postfix_sum[i + 1] + nums[i]

        print(postfix_sum)
        prefix_sum = 0

        for j in range(n):
            if prefix_sum == postfix_sum[j + 1]:
                return j
            prefix_sum += nums[j]
        
        return -1