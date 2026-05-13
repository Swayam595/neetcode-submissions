class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.__findDuplicateBruteForce(nums)
    
    # TC - O(n) SC - O(n)
    def __findDuplicateBruteForce(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num) 