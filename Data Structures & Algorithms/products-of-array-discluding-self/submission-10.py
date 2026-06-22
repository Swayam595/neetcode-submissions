class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_product = [1]
        prev = nums[0]
        ans = [0] * N

        for i in range(1, N):
            prefix_product.append(prev)
            prev *= nums[i]
        
        postfix_product = 1

        for j in range(N - 1, -1, -1):
            ans[j] = postfix_product * prefix_product[j]
            postfix_product *= nums[j]
        
        return ans
