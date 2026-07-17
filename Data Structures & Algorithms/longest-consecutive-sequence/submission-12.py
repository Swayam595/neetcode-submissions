class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return self.__longestConsecutiveUsingHashSet(nums)
        return self.__longestConsecutiveUsingHashMap(nums)
    
    def __longestConsecutiveUsingHashSet(self, nums: List[int]) -> int:
        hash_set = set()
        max_streak = 0

        for num in nums:
            hash_set.add(num)
        
        for num in nums:
            if num - 1 not in hash_set:
                curr_streak = 0
                curr_num = num
                while curr_num in hash_set:
                    curr_streak += 1
                    curr_num += 1
                max_streak = max(max_streak, curr_streak)
        
        return max_streak
    
    def __longestConsecutiveUsingHashMap(self, nums: List[int]) -> int:
        freq_dict = defaultdict(int)
        max_streak = 0

        for num in nums:
            if not freq_dict[num]:
                freq_dict[num] = freq_dict[num - 1] + freq_dict[num + 1] + 1
                freq_dict[num - freq_dict[num - 1]] = freq_dict[num]
                freq_dict[num + freq_dict[num + 1]] = freq_dict[num]
                max_streak = max(max_streak, freq_dict[num])
            
        return max_streak
