class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        # self.__combination_sum_helper1(0, nums, target, ans, [])
        self.__combination_sum_helper2(0, 0, sorted(nums), target, ans, [])
        return ans

    # TC -> O(2 ^ (T / M))
    # SC -> O(T / M)
    # M -> min value in nums
    # T -> Tagert value
    def __combination_sum_helper2(self, i: int, curr_sum: int, nums: List[int], target: int,
                                          ans: List[List[int]], acc: List[int]) -> None:
        if curr_sum == target:
            ans.append(acc.copy())
            return
        
        for j in range(i, len(nums)):
            if curr_sum + nums[j] > target:
                return
                
            acc.append(nums[j])
            curr_sum += nums[j]
            self.__combination_sum_helper2(j, curr_sum, nums, target, ans, acc)

            acc.pop()
            curr_sum -= nums[j]

        return
    
    # TC -> O(2 ^ (T / M))
    # SC -> O(T / M)
    # M -> min value in nums
    # T -> Tagert value
    def __combination_sum_helper1(self, i: int, nums: List[int], target: int,
                                          ans: List[List[int]], acc: List[int]) -> None:
        if i >= len(nums) or target < 0:
            return
        
        if target == 0:
            ans.append(acc.copy())
            return
        
        acc.append(nums[i])
        self.__combination_sum_helper1(i, nums, target - nums[i], ans, acc)

        acc.pop()
        self.__combination_sum_helper1(i + 1, nums, target, ans, acc)

        return