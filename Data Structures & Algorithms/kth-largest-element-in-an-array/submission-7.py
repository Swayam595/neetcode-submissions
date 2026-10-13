class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.__find_kth_largest_min_heap(nums, k)
        return self.__find_kth_largest_quick_select(nums, k)

    # TC -> Average O(n), worst O(n²) (adversarial pivots — e.g., sorted input).
    # SC -> O(1)
    def __find_kth_largest_quick_select(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        L, R = 0, n - 1
        pivot = n

        while L < R:
            pivot = self.__partition(L, R, nums)
            
            if pivot < target:
                L = pivot + 1
            elif pivot > target:
                R = pivot - 1
            else:
                break
                
        return nums[target]
    
    def __partition(self, l: int, r: int, nums: List[int]) -> int:
        pivot_idx = r
        pivot_val = nums[pivot_idx]
        i = l

        for j in range(l, r):
            if nums[j] <= pivot_val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i


    # TC -> O(N * log(K))
    # SC -> O(K)
    # N -> # of elements in the nums array
    # K -> Kth largest element
    def __find_kth_largest_min_heap(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return min_heap[0]