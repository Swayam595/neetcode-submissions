class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return self.__find_min_brute_force(nums)
        return self.__find_min_binary_search(nums)
    
    # TC - O(log(N))
    # SC - O(1)
    # N -> len of nums
    def __find_min_binary_search(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        while l < h:
            mid = l + (h - l) // 2
            if nums[h] < nums[mid]:
                l = mid + 1
            else:
                h = mid
        
        return nums[l]
    
    # TC - O(N)
    # SC - O(1)
    # N -> len of nums
    def __find_min_brute_force(self, nums: List[int]) -> int:
        min_val = float('inf')
        for num in nums:
            min_val = min(min_val, num)
        
        return min_val