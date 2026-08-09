class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # return self.__brute_force(nums)
        # return self.__prefix_suffix_product(nums)
        return self.__prefix_suffix_product_optimized(nums)
    
    # TC -> O(N)
    # SC -> O(1)
    # N -> len of nums
    def __prefix_suffix_product_optimized(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = nums[0]

        prefix_product = 0
        suffix_product = 0

        for i in range(n):
            prefix_product = nums[i] * (prefix_product or 1)
            suffix_product = nums[n - 1 - i] * (suffix_product or 1)

            max_product = max(max_product, max(prefix_product, suffix_product))

        return max_product

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def __prefix_suffix_product(self, nums: List[int]) -> int:
        n = len(nums)

        suffix_product = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]

        prefix_product = 0

        max_product = nums[0]

        for i in range(n):
            prefix_product = nums[i] * (prefix_product or 1)

            max_product = max(max_product, max(prefix_product, suffix_product[i]))

        return max_product
    
    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of nums
    def __brute_force(self, nums: List[int]) -> int:
        ans = nums[0]

        for i in range(len(nums)):
            curr = nums[i]
            ans = max(ans, curr)
            for j in range(i + 1, len(nums)):
                curr = curr * nums[j]
                ans = max(curr, ans)
        
        return ans