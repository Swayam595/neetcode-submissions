class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.__productExceptSelfUsingTwoExtraArray(nums)

    def __productExceptSelfUsingTwoExtraArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix_product = [1] * n
        suffix_product = [1] * n

        for i in range(1, n):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
        
        for j in range(n - 2, -1, -1):
            suffix_product[j] = suffix_product[j + 1] * nums[j + 1]
        
        for k in range(n):
            ans[k] = prefix_product[k] * suffix_product[k]
        
        return ans

    def __productExceptSelfUsingOneExtraArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = 1

        for i in range(1, n):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
        
        for j in range(n - 2, -1, -1):
            suffix_product = suffix_product * nums[j + 1]
            prefix_product[j] = prefix_product[j] * suffix_product
        
        return prefix_product