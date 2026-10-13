class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.__find_kth_largest_min_heap(nums, k)

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