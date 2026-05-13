class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # return self.__subarraySumBruteForce(nums, k) # Time Limit Exceeded
        # return self.__subarraySumPrefixSum(nums, k) # Time Limit Exceeded
        return self.__subarraySumHashMap(nums, k)

    # TC - O(n^3) SC - O(1)
    def __subarraySumBruteForce(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for start in range(n - i):
                curr_sum = 0
                for end in range(start, i):
                    curr_sum += nums[end]
                    if curr_sum == k:
                        ans += 1
        
        return ans

    # TC - O(n^2) SC - O(n)
    def __subarraySumPrefixSum(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        prefix_sum = [0] * n

        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for i in range(n):
            for start in range(n - i):
                end = start + i
                if start == 0: 
                    if prefix_sum[end] == k:
                        ans += 1
                elif prefix_sum[end] - prefix_sum[start - 1] == k:
                    ans += 1

        return ans

    # TC - O(n) SC - O(n)
    def __subarraySumHashMap(self, nums: List[int], k: int) -> int:
        count = 0

        curr_sum = 0
        hash_map = {0: 1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            count += hash_map.get(diff, 0)
            hash_map[curr_sum] = 1 + hash_map.get(curr_sum, 0)
        
        return count

