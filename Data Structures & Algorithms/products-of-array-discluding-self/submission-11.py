class Solution:
    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1]

        for i in range(n - 1):
            product = prefix_product[-1] * nums[i]
            prefix_product.append(product)
        
        suffix_product = 1
        
        for i in range(n - 1, -1, -1):
            prefix_product[i] *= suffix_product
            suffix_product *= nums[i]
        
        return prefix_product