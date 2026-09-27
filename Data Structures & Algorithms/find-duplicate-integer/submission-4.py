class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # return self.__find_duplicate_hash_map(nums)
        return self.__find_duplicate_slow_fast(nums)

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of nums
    def __find_duplicate_slow_fast(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def __find_duplicate_hash_map(self, nums: List[int]) -> int:
        seen = set()

        for val in nums:           
            if val in seen:
                return val

            seen.add(val) 