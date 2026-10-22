class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        self.__dfs(0, sorted(candidates), target, [], 0, ans)
        return [list(comb) for comb in ans]

    # TC -> O(N * 2 ^ N)
    # SC -> O(N * 2 ^ N)
    def __dfs(self, i, nums, target, acc, total, ans):
        if total == target:
            ans.add(tuple(acc))
            return
        
        if i >= len(nums) or total > target:
            return
        
        acc.append(nums[i])
        self.__dfs(i + 1, nums, target, acc, total + nums[i], ans)

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        acc.pop()
        self.__dfs(i + 1, nums, target, acc, total, ans)

        return

