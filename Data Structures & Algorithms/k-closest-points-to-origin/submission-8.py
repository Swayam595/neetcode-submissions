import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return self.__k_closest_max_heap(points, k)
        return self.__k_closest_quick_select(points, k)

    # TC -> O(N) in average case, O(N^2) in worst case
    # SC -> O(1)
    def __k_closest_quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.__euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = self.__partition(L, R, points)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1

        return points[:k]
    
    def __partition(self, l: int, r: int, points: List[List[int]]) -> int:
        pivot_idx = r
        pivot_dist = self.__euclidean(points[pivot_idx])
        i = l

        for j in range(l, r):
            if self.__euclidean(points[j]) <= pivot_dist:
                points[i], points[j] = points[j], points[i]
                i += 1

        points[i], points[r] = points[r], points[i]
        return i
        
    # TC -> O(N * log(K))
    # SC -> O(K)
    # N -> len of the points array
    # K -> integer given or the len of the max heap
    def __k_closest_max_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        max_heap = []

        for x, y in points:
            distance = ((x ** 2) + (y ** 2)) ** 0.5
            heapq.heappush(max_heap, [-1 * distance, [x, y]])

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        while len(max_heap) > 0:
            dist, points = heapq.heappop(max_heap)
            ans.append(points)
        
        return ans