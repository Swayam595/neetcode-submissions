class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # return self.__containsNearbyDuplicateBruteForce(nums, k) # Accepted
        return self.__containsNearbyDuplicateOptimized(nums, k)
    
    # TC - O(n*k) SC - O(1)
    def __containsNearbyDuplicateBruteForce(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for L in range(n):
            for R in range(L + 1, min(L + k + 1, n)):
                if nums[L] == nums[R]:
                    return True
        
        return False
    
    # TC - O(n) SC - O(k)
    def __containsNearbyDuplicateOptimized(self, nums: List[int], k: int) -> bool:
        window = set()

        L = 0
        R = 0

        while R < len(nums):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            
            window.add(nums[R])
            R += 1
        
        return False
