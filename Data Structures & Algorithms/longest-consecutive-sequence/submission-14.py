class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return self.__longest_consecutive_brute_force(nums)
        return self.__longest_consecutive_using_hash_set(nums)
    
    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums array
    def __longest_consecutive_using_hash_set(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_len = max(max_len, length)

        return max_len

    # TC -> O(N ^ 2)
    # SC -> O(N)
    def __longest_consecutive_brute_force(self, nums: List[int]) -> int:
        max_len = 0
        store = set(nums)

        for num in nums:
            curr = num
            streak = 0
            while curr in store:
                streak += 1
                curr += 1
            max_len = max(max_len, streak)
        
        return max_len