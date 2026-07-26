class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        # self.__combinationSumHelper1(0, nums, target, ans, [], 0)
        self.__combinationSumHelper2(0, nums, target, ans, [], 0)
        return ans
    
    def __combinationSumHelper1(self, i: int, nums: List[int], target: int, ans: List[List[int]], acc: List[int], curr_sum: int) -> None:
        if i >= len(nums) or curr_sum > target:
            return
        
        if curr_sum == target:
            ans.append(acc.copy())
            return
        
        acc.append(nums[i])
        curr_sum = curr_sum + nums[i]
        take = self.__combinationSumHelper1(i, nums, target, ans, acc, curr_sum)

        acc.pop()
        curr_sum = curr_sum - nums[i]
        skip = self.__combinationSumHelper1(i + 1, nums, target, ans, acc, curr_sum)
        
        return

    def __combinationSumHelper2(self, i: int, nums: List[int], target: int, ans: List[List[int]], acc: List[int], curr_sum: int) -> None:
        if curr_sum == target:
            ans.append(acc.copy())
            return
        
        if i >= len(nums) or curr_sum > target:
            return

        for j in range(i, len(nums)):
            acc.append(nums[j])
            curr_sum += nums[j]
            self.__combinationSumHelper2(j, nums, target, ans, acc, curr_sum)

            acc.pop()
            curr_sum -= nums[j]

        return
