class Solution:
    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False