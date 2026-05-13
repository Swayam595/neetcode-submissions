class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return self.__productExceptSelfBruteForce(nums) # Accepted but inefficient
        return self.__productExceptSelfPrefixProduct(nums) # Accepted

    # TC - O(n^2) SC - O(1)
    def __productExceptSelfBruteForce(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        running_prod = 1

        for i in range(n):
            curr_prod = 1
            for j in range(i + 1, n):
                curr_prod *= nums[j]
            ans.append(running_prod * curr_prod)
            running_prod *= nums[i]
        
        return ans
    
    def __productExceptSelfPrefixProduct(self, nums: List[int]) -> List[int]:
        ans = []

        n = len(nums)
        prefix_product = [1] * n
        
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        postfix_product = 1

        for j in range(n - 1, -1, -1):
            curr_product = prefix_product[j] * postfix_product
            ans.append(curr_product)
            postfix_product *= nums[j]

        return ans[::-1]