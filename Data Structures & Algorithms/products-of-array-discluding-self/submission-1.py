class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = 1

        for i in range(1, n):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
        
        for j in range(n - 2, -1, -1):
            suffix_product = suffix_product * nums[j + 1]
            prefix_product[j] = prefix_product[j] * suffix_product
        
        
        return prefix_product