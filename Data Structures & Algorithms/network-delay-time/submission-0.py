class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time_to_signal = 0

        adjacency_list = dict()
        visited = set()
        min_heap = []
        shortest_path = dict()

        for i in range(1, n + 1):
            adjacency_list[i] = []
        
        for s, d, w in times:
            adjacency_list[s].append((d, w))
        
        heapq.heappush(min_heap, (0, k))

        while len(min_heap) > 0:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue
            
            shortest_path[n1] = w1
            visited.add(n1)

            for n2, w2 in adjacency_list[n1]:
                if n2 not in visited:
                    cost = w1 + w2
                    heapq.heappush(min_heap, (cost, n2))
        
        for i in range(1, n + 1):
            if i not in visited:
                return -1
            min_time_to_signal = max(min_time_to_signal, shortest_path[i])
        
        return min_time_to_signal