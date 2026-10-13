class Solution:
    # TC - O(N * 2 ^ N)
    # 2^N recursive calls (one per subset), but each leaf does
    # ans.append(list(acc)), which copies the current subset of size up to
    # N. So the copying work is O(N) per leaf → O(N · 2^N).
    
    # SC - O(H) ~ O(N)
    # H - height of the decision tree which is equal to N
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.__subsets_helper(0, nums, [], ans)
        return ans
    
    def __subsets_helper(self, i: int, nums: List[int], acc: List[int], ans: List[int]) -> None:
        if i >= len(nums):
            ans.append(acc.copy())
            return
        
        acc.append(nums[i])
        self.__subsets_helper(i + 1, nums, acc, ans)

        acc.pop()
        self.__subsets_helper(i + 1, nums, acc, ans)
        return
