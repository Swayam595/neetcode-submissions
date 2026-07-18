class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.__findMinBruteForce(nums)
        # return 
    
    # TC - O(N)
    # SC - O(1)
    def __findMinBruteForce(self, nums: List[int]) -> int:
        min_value = float('inf')
        for num in nums:
            min_value = min(min_value, num)
        
        return min_value