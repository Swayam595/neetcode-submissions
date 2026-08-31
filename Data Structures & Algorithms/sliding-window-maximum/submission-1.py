class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return self.__max_sliding_window_brute_force(nums, k)
        return self.__max_sliding_window_deque(nums, k)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of nums
    def __max_sliding_window_deque(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        l = 0
        r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1

        return ans


    # TC -> O(N * K)
    # SC -> O(1)
    def __max_sliding_window_brute_force(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            curr_max = -float('inf')
            for j in range(i, min(i + k, len(nums))):
                curr_max = max(curr_max, nums[j])
            
            ans.append(curr_max)
        
        return ans