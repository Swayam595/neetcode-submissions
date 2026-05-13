class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return self.__minSubArrayLenBruteForce(target, nums)

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