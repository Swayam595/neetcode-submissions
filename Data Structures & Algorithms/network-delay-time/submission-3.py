class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return self.__dijkstra(times, n, k)

    # TC -> O(V + V * log(E)) ~ O(V * log(E))
    # SC -> O(V)
    # V -> # of vertices
    # E -> # of edges
    def __dijkstra(self, times: List[List[int]], n: int, k: int) -> int:
        adj_dict = self.__create_adj_dict(times, n)
        min_heap = []
        heapq.heappush(min_heap, [0, k])
        seen = set()
        total_time = 0

        while len(min_heap) > 0:
            time, node = heapq.heappop(min_heap)

            if node in seen:
                continue

            seen.add(node)
            total_time = time
            for neighbor, dist in adj_dict[node]:
                heapq.heappush(min_heap, [time + dist, neighbor])
        
        return total_time if len(seen) == n else -1

    def __create_adj_dict(self, times: List[List[int]], n: int) -> dict[int, List[List[int, int]]]:
        adj_dict = {i: [] for i in range(1, n + 1)}
        for u, v, d in times:
            adj_dict[u].append([v, d])
        return adj_dict