class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.__recursive(0, nums, target, 0)
    
    def __recursive(self, i:int, nums: List[int], target: int, total_sum: int) -> int:
        if i == len(nums):
            if total_sum == target:
                return 1
            else:
                return 0
        
        add = self.__recursive(i + 1, nums, target, total_sum + nums[i])
        subtract = self.__recursive(i + 1, nums, target, total_sum - nums[i])

        return add + subtract