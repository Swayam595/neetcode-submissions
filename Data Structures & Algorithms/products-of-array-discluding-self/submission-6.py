class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix_product = self._get_prefix_product(nums)
        postfix_product = 1

        for i in range(len(nums) - 1, -1, -1):
            product = prefix_product[i] * postfix_product
            ans.append(product)
            postfix_product *= nums[i]
        
        return ans[::-1]
        
    def _get_prefix_product(self, nums):
        n = len(nums)
        prefix_product = [1] * n

        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        return prefix_product