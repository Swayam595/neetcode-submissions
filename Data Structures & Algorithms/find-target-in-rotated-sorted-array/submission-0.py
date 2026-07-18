class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.__searchBruteForce(nums, target)
    
    # TC - O(N)
    # SC - O(1)
    # N -> len of nums
    def __searchBruteForce(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1