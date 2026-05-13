class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.__helper1(0, nums)

    # TC - O(n^2 * n!)
    # SC - O(n * n!)
    def __helper1(self, i: int, nums: List[int]) -> List[List[int]]:
        if i == len(nums):
            return [[]]

        perms = self.__helper1(i + 1, nums)
        nextPerms = []

        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                nextPerms.append(pCopy)
        
        return nextPerms