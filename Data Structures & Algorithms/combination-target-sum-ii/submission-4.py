class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # return self.__dfs1(candidates, target)
        return self.__dfs2(candidates, target)

    def __dfs2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.__dfs2_helper(0, sorted(nums), target, [], 0, ans)
        return ans
    
    # TC -> O(N * 2 ^ N)
    # SC -> O(N)
    def __dfs2_helper(self, i, nums, target, acc, total, ans):
        if target == total:
            ans.append(acc.copy())
            return
        
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            
            if total + nums[j] > target:
                return
            
            acc.append(nums[j])
            self.__dfs2_helper(j + 1, nums, target, acc, total + nums[j], ans)
            acc.pop()

        return

    # TC -> O(N * 2 ^ N)
    # SC -> O(N * 2 ^ N)
    def __dfs1(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        self.__dfs1_helper(0, sorted(nums), target, [], 0, ans)
        return [list(comb) for comb in ans]

    def __dfs1_helper(self, i, nums, target, acc, total, ans):
        if total == target:
            ans.add(tuple(acc))
            return
        
        if i >= len(nums) or total > target:
            return
        
        acc.append(nums[i])
        self.__dfs1_helper(i + 1, nums, target, acc, total + nums[i], ans)

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        acc.pop()
        self.__dfs1_helper(i + 1, nums, target, acc, total, ans)

        return

