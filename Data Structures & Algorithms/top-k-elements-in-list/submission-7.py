class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self._min_heap_solution(nums, k)
        return self._bucket_sort_solution(nums, k)

    def _bucket_sort_solution(self, nums, k):
        ans = []
        freq_dict = self._get_freq_dict(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in freq_dict.items():
            bucket[freq].append(num)

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans

    def _min_heap_solution(self, nums, k):
        freq_dict = self._get_freq_dict(nums)
        return self._get_top_k_frequent_elements(freq_dict, k)

    def _get_freq_dict(self, nums):
        freq_dict = dict()
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1
        return freq_dict
    
    def _get_top_k_frequent_elements(self, freq_dict, k):
        ans = []
        min_heap = []
        print (freq_dict)
        for num, curr_num_freq in freq_dict.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (curr_num_freq, num))
            else:
                front_num_freq = min_heap[0][0]
                if front_num_freq < curr_num_freq:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (curr_num_freq, num))

        while len(min_heap) > 0:
            freq, num = heapq.heappop(min_heap)
            ans.append(num)
        
        return ans