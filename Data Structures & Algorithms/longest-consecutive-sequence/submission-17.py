class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return self.__longest_consecutive_brute_force(nums)
        # return self.__longest_consecutive_using_hash_set(nums)
        return self.__longest_consecutive_using_hash_map(nums)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums array
    def __longest_consecutive_using_hash_map(self, nums: List[int]) -> int:
        num_set = dict()
        max_len = 0

        for num in nums:
            if num not in num_set:
                num_set[num] = 1 + num_set.get(num - 1, 0) + num_set.get(num + 1, 0)
                num_set[num - num_set.get(num - 1, 0)] = num_set[num]
                num_set[num + num_set.get(num + 1, 0)] = num_set[num]
                max_len = max(max_len, num_set[num])
             
        return max_len
    
    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums array
    def __longest_consecutive_using_hash_set(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in num_set:
                streak = 0
                while num + streak in num_set:
                    streak += 1
                max_len = max(max_len, streak)
        
        return max_len
            

    # TC -> O(N ^ 2)
    # SC -> O(N)
    def __longest_consecutive_brute_force(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)

        for num in nums:
            curr = num
            streak = 0
            while curr + streak in num_set:
                streak += 1
            max_len = max(max_len, streak)
        
        return max_len