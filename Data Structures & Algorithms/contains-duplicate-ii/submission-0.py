class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return self.__containsNearbyDuplicateBruteForce(nums, k)
    
    # TC - O(n*k) SC - O(1)
    def __containsNearbyDuplicateBruteForce(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for L in range(n):
            for R in range(L + 1, min(L + k + 1, n)):
                if nums[L] == nums[R]:
                    return True
        
        return False