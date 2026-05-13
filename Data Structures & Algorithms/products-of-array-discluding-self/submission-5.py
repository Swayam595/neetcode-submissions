class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        postfix_product = 1

        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        for j in range(n - 1, -1, -1):
            ans[j] = ans[j] * postfix_product
            postfix_product = postfix_product * nums[j]
        
        return ans