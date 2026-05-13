class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return self.__helper1(0, nums)
        return self.__helper2(nums)

    # TC - O(n^2 * n!)
    # SC - O(n * n!)
    def __helper1(self, i: int, nums: List[int]) -> List[List[int]]:
        if i == len(nums):
            return [[]]

        perms = self.__helper1(i + 1, nums)
        next_perms = []

        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, nums[i])
                next_perms.append(pCopy)
        
        return next_perms
    
    def __helper2(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            next_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    next_perms.append(p_copy)
            perms = next_perms
        
        return perms