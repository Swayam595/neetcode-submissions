class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return self.__findMinBruteForce(nums)
        return self.__findMinBinarySerach(nums)
    
    # TC - O(N)
    # SC - O(1)
    def __findMinBruteForce(self, nums: List[int]) -> int:
        min_value = float('inf')
        for num in nums:
            min_value = min(min_value, num)
        
        return min_value
    
    def __findMinBinarySerach(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]