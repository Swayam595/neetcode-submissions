import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        max_heap = []

        for x, y in points:
            distance = ((x ** 2) + (y ** 2)) ** 0.5
            heapq.heappush(max_heap, [-1 * distance, [x, y]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        while len(max_heap) > 0:
            top = heapq.heappop(max_heap)
            ans.append(top[1])
        
        return ans