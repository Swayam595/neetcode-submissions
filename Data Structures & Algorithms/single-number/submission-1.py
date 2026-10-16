class Solution:
    # TC -> O(N)
    # SC -> O(1)
    # N -> len of nums array
    def singleNumber(self, nums: List[int]) -> int:
        curr = 0

        for num in nums:
            curr = curr ^ num
        
        return curr