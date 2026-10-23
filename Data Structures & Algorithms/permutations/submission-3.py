class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.__permute1(nums)
    
    def __permute1(self, nums: List[int]) -> List[List[int]]:
        return self.__permute_helper1(0, nums)

    def __permute_helper1(self, i: int, nums: List[int]) -> List[List[int]]:
        if i >= len(nums):
            return [[]]
        
        perms = self.__permute_helper1(i + 1, nums)
        next_perms = []

        for p in perms:
            for j in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(j, nums[i])
                next_perms.append(p_copy)
        
        return next_perms