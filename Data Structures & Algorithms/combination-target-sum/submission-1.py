class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        self.__helper1(0, 0, [], combs, nums, target)
        return combs
    
    def __helper1(self, i: int, curr_sum: int, curr_comb: List[int], 
                        combs: List[List[int]], nums: List[int], target: int) -> None:
        if curr_sum == target:
            combs.append(curr_comb.copy())
            return
        
        if i >= len(nums) or curr_sum > target:
            return
        
        curr_comb.append(nums[i])
        curr_sum += nums[i]
        self.__helper1(i, curr_sum, curr_comb, combs, nums, target)

        curr_comb.pop()
        curr_sum -= nums[i]
        self.__helper1(i + 1, curr_sum, curr_comb, combs, nums, target)
        return
        