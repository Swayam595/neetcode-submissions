class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return self.__permute1(nums)
        # return self.__permute2(nums)
        return self.__permute3(nums)

    # TC - O(n * n!)
    # SC - O(n * n!)
    def __permute3(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.__permute3_back_tracking([], nums, [False for _ in range(len(nums))], ans)
        return ans
    
    def __permute3_back_tracking(self, acc: List[int], nums: List[int], pick: List[bool], ans: List[List[int]]) -> None:
        if len(acc) == len(nums):
            ans.append(acc.copy())
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                acc.append(nums[i])
                pick[i] = True
                self.__permute3_back_tracking(acc, nums, pick, ans)

                acc.pop()
                pick[i] = False
        
        return

    # TC - O(n^2 * n!)
    # SC - O(n!)
    def __permute2(self, nums: List[int]) -> List[List[int]]:
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
    
    # TC - O(n^2 * n!)
    # SC - O(n * n!)
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