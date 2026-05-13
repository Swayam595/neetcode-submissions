class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
        max_heap = []
        print (freq_dict)
        for num, curr_num_freq in freq_dict.items():
            if len(max_heap) < k:
                heapq.heappush(max_heap, (curr_num_freq, num))
            else:
                front_num_freq = max_heap[0][0]
                if front_num_freq < curr_num_freq:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (curr_num_freq, num))

        while len(max_heap) > 0:
            freq, num = heapq.heappop(max_heap)
            ans.append(num)
        
        return ans