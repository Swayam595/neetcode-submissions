class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return self.__search_brute_force(nums, target)
        return self.__search_binary_search(nums, target)
        # return self.__searchBinarySearchOptimized(nums, target)

    # TC - O(log(N))
    # SC - O(1)
    # N -> len of nums
    def __search_binary_search(self, nums: List[int], target: int) -> int:
        l, h = self.__find_search_space(nums, target)

        while l <= h:
            mid = l + (h - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return -1

    def __find_search_space(self, nums: List[int], target: int) -> tuple(int, int):
        rotation_point = self.__find_rotation_point(nums)

        if nums[rotation_point] <= target and target <= nums[-1]:
            return [rotation_point, len(nums) - 1]
        else:
            return (0, rotation_point)

    # TC - O(log(N))
    # SC - O(1)
    # N -> len of nums
    def __find_rotation_point(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        while l < h:
            mid = l + (h - l) // 2
            if nums[h] < nums[mid]:
                l = mid + 1
            else:
                h = mid
        return l
    
    # TC - O(N)
    # SC - O(1)
    # N -> len of nums
    def __search_brute_force(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
