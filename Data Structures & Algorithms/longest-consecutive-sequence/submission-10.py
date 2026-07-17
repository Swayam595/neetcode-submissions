class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        max_len = 0
        for num in nums:
            hash_set.add(num)
        
        i = 0
        while i < len(nums):
            if nums[i] - 1 not in hash_set:
                curr_num = nums[i]
                curr_len = 0
                while curr_num in hash_set:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
            i += 1
        
        return max_len
