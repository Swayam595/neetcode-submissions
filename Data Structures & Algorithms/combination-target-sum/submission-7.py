class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.__combination_sum_recursive(0, nums, target, ans, [])
        return ans
    
    # TC -> O(2 ^ N)
    # SC -> O(T)
    # N -> len of nums
    # T -> Tagert value
    def __combination_sum_recursive(self, i: int, nums: List[int], target: int,
                                          ans: List[List[int]], acc: List[int]) -> None:
        if i >= len(nums) or target < 0:
            return
        
        if target == 0:
            ans.append(acc.copy())
            return
        
        acc.append(nums[i])
        self.__combination_sum_recursive(i, nums, target - nums[i], ans, acc)

        acc.pop()
        self.__combination_sum_recursive(i + 1, nums, target, ans, acc)

        return