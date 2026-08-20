class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.__brute_force(nums, k)

    # TC -> O(N + M * log(K) + log(K)) -> O(M * log(K))
    # SC -> O(max(M + K))
    # N -> Len of the nums
    # M -> # of unique elements
    # K -> # of most frequent elements 
    def __brute_force(self, nums: List[int], k: int) -> List[int]:
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
