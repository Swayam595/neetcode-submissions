class Solution:
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # return self.__subsets_with_dup_recursion(nums)
        return self.__subsets_with_dup_iteration(nums)
    
    # TC -> O(n * 2 ^ N)
    # N -> Len of the nums list 
    # O(N) -> copying a subset
    # O(2 ^ N) -> Number of iteration on subsets
    # SC -> O(2 ^ N)
    # O(2^n): Output space storing all subsets (up to 2^n subsets)
    def __subsets_with_dup_iteration(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        ans = [[]]
        idx = 0
        prev_idx = 0

        for i in range(len(nums_sorted)):
            idx = prev_idx if i >= 1 and nums_sorted[i] == nums_sorted[i - 1] else 0
            prev_idx = len(ans)

            for j in range(idx, prev_idx):
                subset = ans[j].copy()
                subset.append(nums_sorted[i])
                ans.append(subset)
            
        return ans
    
    # TC -> O(n * 2 ^ N)
    # N -> Len of the nums list 
    # O(N) -> copying a subset
    # O(2 ^ N) -> Number of recursive calls
    # SC -> O(n + 2 ^ N)
    # O(n): Recursion call stack depth (at most n levels deep)
    # O(2^n): Output space storing all subsets (up to 2^n subsets)
    def __subsets_with_dup_recursion(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        self.__subsets_with_dup_recursion_helper(0, sorted(nums), [], ans)
        return ans

   
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