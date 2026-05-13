class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return self.__minSubArrayLenBruteForce(target, nums) #Accepted
        return self.__minSubArrayLenSlidingWindow(target, nums)

    # TC - O(n^2) SC - O(1)
    def __minSubArrayLenBruteForce(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum >= target:
                    min_len = min(min_len, j - i + 1)
                    break
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len

    def __minSubArrayLenSlidingWindow(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')

        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]

            while curr_sum >= target:
                min_len = min(min_len, R - L + 1)
                curr_sum -= nums[L]
                L += 1

        if min_len == float('inf'):
            return 0
        else: 
            return min_len