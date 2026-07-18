class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return self.__searchBruteForce(nums, target)
        return self.__searchBinarySearch(nums, target)
    
    # TC - O(N)
    # SC - O(1)
    # N -> len of nums
    def __searchBruteForce(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
    
    # TC - O(logN)
    # SC - O(1)
    # N -> len of nums
    def __searchBinarySearch(self, nums: List[int], target: int) -> int:
        l, r = self.__findSearchSpaceIndex(nums, target)
        
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            
        return -1

    def __findSearchSpaceIndex(self, nums: List[int], target: int) -> [int, int]:
        rotation_point = self.__findPointOfRoration(nums)

        if nums[rotation_point] <= target and target <= nums[-1]:
            return rotation_point, len(nums)
        else:
            return 0, rotation_point - 1
    
    def __findPointOfRoration(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return l