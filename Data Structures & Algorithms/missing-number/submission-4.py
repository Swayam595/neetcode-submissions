class Solution:
    # TC -> O(n)
    # SC -> O(1)
    # n -> len of nums array
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n

        for i in range(n):
            xor = xor ^ i ^ nums[i]
        
        return xor