class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.__find_duplicate_hash_map(nums)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def __find_duplicate_hash_map(self, nums: List[int]) -> int:
        seen = set()

        for val in nums:           
            if val in seen:
                return val

            seen.add(val) 