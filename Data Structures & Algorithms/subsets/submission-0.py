class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.__ans = []
        self.__getSubsets(nums, 0, [])
        return self.__ans
    
    def __getSubsets(self, nums, i, acc):
        if len(nums) <= i:
            self.__ans.append(acc.copy())
            return
        
        acc.append(nums[i])
        self.__getSubsets(nums, i + 1, acc)

        acc.pop()
        self.__getSubsets(nums, i + 1, acc)
        return