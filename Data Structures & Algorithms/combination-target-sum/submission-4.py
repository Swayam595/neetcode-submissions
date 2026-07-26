class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.__combinationSumHelper(0, nums, target, ans, [], 0)
        return ans
    
    def __combinationSumHelper(self, i: int, nums: List[int], target: int, ans: List[List[int]], acc: List[int], curr_sum: int) -> None:
        if i >= len(nums) or curr_sum > target:
            return
        
        if curr_sum == target:
            ans.append(list(acc))
            return
        
        acc.append(nums[i])
        take = self.__combinationSumHelper(i, nums, target, ans, acc, curr_sum + nums[i])

        acc.pop()
        skip = self.__combinationSumHelper(i + 1, nums, target, ans, acc, curr_sum)
        
        return