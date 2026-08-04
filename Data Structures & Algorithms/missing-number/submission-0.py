class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans ^ num
        
        for num in range(len(nums) + 1):
            ans = ans ^ num
        
        return ans