class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.__subsets_with_dup_recursion(nums)

    def __subsets_with_dup_recursion(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        self.__subsets_with_dup_recursion_helper(0, sorted(nums), [], ans)
        return ans

    # TC -> O(2 ^ N)
    # SC -> O(2 ^ N)
    # N -> Len of the nums list    
    def __subsets_with_dup_recursion_helper(self, i: int, nums: List[int], acc: List[int], ans: List[List[int]]) -> None:
        if i >= len(nums):
            ans.append(acc.copy())
            return
        
        acc.append(nums[i])
        self.__subsets_with_dup_recursion_helper(i + 1, nums, acc, ans)

        acc.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.__subsets_with_dup_recursion_helper(i + 1, nums, acc, ans)
        return