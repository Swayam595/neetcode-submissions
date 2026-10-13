class Solution:
    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of the nums array
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.__subsets_helper(0, nums, [], ans)
        return ans
    
    def __subsets_helper(self, i: int, nums: List[int], acc: List[int], ans: List[int]) -> None:
        if i >= len(nums):
            ans.append(list(acc))
            return
        
        acc.append(nums[i])
        self.__subsets_helper(i + 1, nums, acc, ans)

        acc.pop()
        self.__subsets_helper(i + 1, nums, acc, ans)
        return
