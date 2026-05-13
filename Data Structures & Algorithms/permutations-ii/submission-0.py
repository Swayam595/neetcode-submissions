class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.__ans = []
        count = dict()
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        self.__dfs([], nums, count)
        return self.__ans
    
    def __dfs(self, perm: List[int], nums: List[int], count: dict) -> None:
        if len(perm) == len(nums):
            self.__ans.append(perm.copy())
            return
        
        for n in count:
            if count[n] > 0:
                count[n] -= 1
                perm.append(n)

                self.__dfs(perm, nums, count)

                perm.pop()
                count[n] += 1

        return