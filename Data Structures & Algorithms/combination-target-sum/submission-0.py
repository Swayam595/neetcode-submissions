class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.__ans = []
        self.__getCombination(nums, [], 0, target, 0)
        return self.__ans
    
    def __getCombination(self, nums, acc, curr_sum, target, i):
        if curr_sum == target:
            self.__ans.append(acc.copy())
            return

        if len(nums) <= i or curr_sum > target:
            return

        curr_val = nums[i]
        curr_sum += curr_val
        acc.append(curr_val)
        self.__getCombination(nums, acc, curr_sum, target, i)

        curr_sum -= curr_val
        acc.pop()
        self.__getCombination(nums, acc, curr_sum, target, i + 1)
        return