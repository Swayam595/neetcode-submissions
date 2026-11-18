class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        return self.__dijkstra(n, flights, src, dst, k)

    # TC -> O(V * log(E))
    # SC -> O(V + E)
    # V -> # of vertices/ airport
    # E -> # of edges/connecting flights
    def __dijkstra(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        adj_dict = self.__get_adj_dict(n, flights)
        dist = [[INF] * (k + 2) for _ in range(n)]

        min_heap = [(0, -1, src)]
        dist[src][0] = 0

        while len(min_heap) > 0:
            current_cost, stops, current_stop = heapq.heappop(min_heap)
            
            if current_stop == dst:
                return current_cost
            
            if stops == k or dist[current_stop][stops + 1] < current_cost:
                continue

            for neighbor, flight_cost in adj_dict[current_stop]:
                next_cost = current_cost + flight_cost
                next_stop = 1 + stops
                if dist[neighbor][next_stop + 1] > next_cost:
                    dist[neighbor][next_stop + 1] = next_cost
                    heapq.heappush(min_heap, (next_cost, next_stop, neighbor))
        
        return -1

    def __get_adj_dict(self, n: int, edges: List[List[int]]) -> dict[int, list[int]]:
        adj_dict = {i: list() for i in range(n)}

        for u, v, w in edges:
            adj_dict[u].append((v, w))
        
        return adj_dict