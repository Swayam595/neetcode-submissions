class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return self.__brute_force(nums)
        # return self.__recursion(0,nums, False)
        # return self.__top_down(nums)
        return self.__bottom_up(nums)
        # return self.__kadnes_algo(nums)

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of nums
    def __kadnes_algo(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        curr_sum = 0

        n = len(nums)

        for i in range(n):
            curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0
            
        
        return max_sum

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def __bottom_up(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[False, False] for _ in range(n)]
        dp[n - 1][0] = nums[n - 1]
        dp[n - 1][1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1])
            dp[i][1] = max(nums[i], nums[i] + dp[i + 1][1])

        return max(dp[0][0], dp[0][1])

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def __top_down(self, nums: List[int]) -> int:
        cache = [[False, False] for _ in range(len(nums))]
        return self.__top_down_helper(0, nums, False, cache)

    def __top_down_helper(self, i: int, nums: List[int], flag: bool, cache: List[dict]) -> int:
        if i == len(nums) - 1:
            return max(0, nums[i]) if flag else nums[i]

        f = 1 if flag else 0

        if cache[i][f]:
            return cache[i][f]

        if flag:
            cache[i][f] = max(0, nums[i] + self.__top_down_helper(i + 1, nums, True, cache))
        else:
            cache[i][f] = max(nums[i] + self.__top_down_helper(i + 1, nums, True, cache), self.__top_down_helper(i + 1, nums, False, cache))

        return cache[i][f]        

    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of nums
    def __recursion(self, i: int, nums: List[int], flag: bool) -> int:
        if i == len(nums) - 1:
            return max(0, nums[i]) if flag else nums[i]
        
        if flag:
            return max(0, nums[i] + self.__recursion(i + 1, nums, True))

        return max(self.__recursion(i + 1, nums, False), nums[i] + self.__recursion(i + 1, nums, True))
    
    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of nums
    def __brute_force(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum 