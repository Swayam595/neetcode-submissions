class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.__brute_force(nums, target)

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of nums
    def __brute_force(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        
        return -1