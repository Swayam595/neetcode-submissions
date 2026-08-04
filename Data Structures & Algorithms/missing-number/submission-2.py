class Solution:
    # TC -> O(n)
    # SC -> O(1)
    # n -> len of nums array
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr = xorr ^ i ^ nums[i]
        return xorr