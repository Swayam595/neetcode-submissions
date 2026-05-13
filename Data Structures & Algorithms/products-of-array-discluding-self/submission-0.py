class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n

        for i in range(1, n):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
        
        for j in range(n - 2, -1, -1):
            suffix_product[j] = nums[j + 1] * suffix_product[j + 1]
        
        for k in range(n):
            prefix_product[k] = prefix_product[k] * suffix_product[k]
        
        return prefix_product