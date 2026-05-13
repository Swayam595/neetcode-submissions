class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # return self.__findDuplicateBruteForce(nums) # Accepted
        # return self.__findDuplicateOptimized(nums) # Accepted
        return self.__findDuplicateSlowFastPointer(nums)
    
    # TC - O(n) SC - O(n)
    def __findDuplicateBruteForce(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num) 
    
    # TC - O(n) SC - O(1)
    def __findDuplicateOptimized(self, nums: List[int]) -> int:
        for i in nums:
            index = abs(i)
            if nums[index] < 0:
                return index
            nums[index] = -1 * nums[index]
    
    # TC - O(n) SC - O(1)
    def __findDuplicateSlowFastPointer(self, nums: List[int]) -> int:
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
