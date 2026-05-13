class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # return self.__findDuplicateBruteForce(nums) # Accepted
        return self.__findDuplicateOptimized(nums)
    
    # TC - O(n) SC - O(n)
    def __findDuplicateBruteForce(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num) 
    
    def __findDuplicateOptimized(self, nums: List[int]) -> int:
        for i in nums:
            index = abs(i)
            if nums[index] < 0:
                return index
            nums[index] = -1 * nums[index]
            