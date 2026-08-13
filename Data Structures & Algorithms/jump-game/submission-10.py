class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return self.__recursive(0, nums)
        # return self.__top_down(nums)
        return self.__bottom_up(nums)

    # TC -> O(N * M)
    # SC -> O(N)
    # N -> Len of nums
    # M -> Max jump lenght in nums
    def __bottom_up(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            jump_length = nums[i]
            for j in range(1, jump_length + 1):
                if i + j >= n - 1:
                    dp[i] = True
                    break
                elif dp[i + j]:
                    dp[i] = True
                    break

        return dp[0]
 
    # TC -> O(N * M)
    # SC -> O(N)
    # N -> Len of nums
    # M -> Max jump lenght in nums
    def __top_down(self, nums: List[int]) -> bool:
        cache = [False] * len(nums)

        return self.__top_down_helper(0, nums, cache)

    def __top_down_helper(self, i: int, nums: List[int], cache: List[bool]) -> bool:
        if i>= len(nums) - 1:
            return True
        
        if cache[i]:
            return cache[i]

        if nums[i] == 0:
            return False
        
        jump_length = nums[i]
        for j in range(1, jump_length + 1):
            if self.__top_down_helper(i + j, nums, cache):
                cache[i] = True
                break

        return cache[i]

    # TC -> O(M ^ N)
    # SC -> O(N)
    # N -> Len of nums
    # M -> Max jump lenght in nums
    def __recursive(self, i: int, nums: List[int]) -> bool:
        if i >= len(nums) - 1:
            return True
        
        if nums[i] == 0:
            return False
        
        jump_length = nums[i]

        for j in range(1, jump_length + 1):
            if self.__recursive(i + j, nums):
                return True
        
        return False