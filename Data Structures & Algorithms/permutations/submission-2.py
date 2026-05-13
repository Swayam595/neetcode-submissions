class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return self.__helper1(0, nums)
        # return self.__helper2(nums)
        return self.__backTracking(nums)

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
    
    # TC - O(n^2 * n!)
    # SC - O(n!)
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

    def __backTracking(self, nums: List[int]) -> List[List[int]]:
        self.__ans = []
        self.__backTrackingHelper([], nums, [False for _ in range(len(nums))])
        return self.__ans
    
    # TC - O(n * n!)
    # SC - O(n * n!)
    def __backTrackingHelper(self, perm: List[int], nums: List[int], pick: List[bool]) -> None:
        if len(perm) == len(nums):
            self.__ans.append(perm.copy())
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.__backTrackingHelper(perm, nums, pick)
                perm.pop()
                pick[i] = False
        
        return
