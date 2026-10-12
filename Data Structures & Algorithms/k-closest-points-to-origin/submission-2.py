class Solution:
    # TC -> O(N * log(K))
    # SC -> O(K)
    # N -> len of the points array
    # K -> integer given
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        max_heap = []

        for x, y in points:
            dist = (x ** 2 + y ** 2) ** 0.5

            if len(max_heap) < k or dist <= -max_heap[0][0]:
                heapq.heappush(max_heap, [-dist, [x, y]])

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        while len(max_heap) > 0:
            dist, points = heapq.heappop(max_heap)
            ans.append(points)
        
        return ans