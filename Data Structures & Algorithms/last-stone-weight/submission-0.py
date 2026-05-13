import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            smash_result = abs(x - y)
            if smash_result > 0:
                heapq.heappush(max_heap, -1 * smash_result)
                
        return 0 if len(max_heap) == 0 else -1 * max_heap[0]