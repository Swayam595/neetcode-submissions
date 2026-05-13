class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return self.__longest_consecutive_brute_force(nums)
        # return self.__longest_consecutive_sorting(nums)
        return self.__longest_consecutive_hashset(nums)

    def __longest_consecutive_brute_force(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            curr, streak = num, 0

            while curr in store:
                streak += 1
                curr += 1
            
            res = max(res, streak)
        
        return res
    
    def __longest_consecutive_sorting(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = 0
        nums.sort()

        curr = nums[0]
        streak = 0
        i = 0

        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        
        return res

    def __longest_consecutive_hashset(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest