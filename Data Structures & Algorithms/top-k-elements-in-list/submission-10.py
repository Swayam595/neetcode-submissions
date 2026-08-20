class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.__brute_force_min_heap(nums, k)
        return self.__optimized_bucket_sort(nums, k)

    # TC -> O(N)
    # SC -> O(N)
    # N -> Len of the nums
    def __optimized_bucket_sort(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq_dict = dict()
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        for num, freq in freq_dict.items():
            bucket[freq].append(num)
            
        for i in range(n, 0, -1): 
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


    # TC -> O(N * log(K))
    # SC -> O(N + K)
    # N -> Len of the nums
    # K -> # of most frequent elements 
    def __brute_force_min_heap(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()
        min_heap = []
        ans = []

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1
        
        for num, count in count_dict.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, [count, num])
            elif len(min_heap) == k and min_heap[0][0] < count:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, [count, num])

        while len(min_heap) > 0:
            count, num = heapq.heappop(min_heap)
            ans.append(num)
        
        return ans
