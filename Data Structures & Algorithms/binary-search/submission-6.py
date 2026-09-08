class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return self.__brute_force(nums, target)
        return self.__binary_search(nums, target)

    # TC -> O(log(N))
    # SC -> O(1)
    # N -> len of nums
    def __binary_search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of nums
    def __brute_force(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        
        return -1