class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # return self.__dijkstra(n, flights, src, dst, k)
        # return self.__bellman_ford(n, flights, src, dst, k)
        return self.__shortest_path_faster_algorithm(n, flights, src, dst, k)

    # TC -> O(k * m)
    # SC -> O(n)
    # n -> # of vertices/ airport
    # m -> # of edges/connecting flights
    # k -> max number of flights allowed
    def __shortest_path_faster_algorithm(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        adj_dict = self.__get_adj_dict(n, flights)

        q = deque([(0, 0, src)])

        while len(q) > 0:
            cost, stops, node = q.popleft()

            if stops > k:
                continue
            
            for neighbor, p in adj_dict[node]:
                next_cost = p + cost
                if next_cost < prices[neighbor]:
                    prices[neighbor] = next_cost
                    q.append((next_cost, stops + 1, neighbor))

        return -1 if prices[dst] == float('inf') else prices[dst]

    # TC -> O(K * (n + m))
    # SC -> O(n)
    # n -> # of vertices/ airport
    # m -> # of edges/connecting flights
    # K -> max number of flights allowed + 1 i.e. k + 1
    def __bellman_ford(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp_prices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            prices = temp_prices
        return -1 if prices[dst] == float('inf') else prices[dst]

    # TC -> O(n*K + m*k*log(m*K)) ~ O(m * K * log(m * K))
    # SC -> O(m + n*K + m*K)
    # n -> # of vertices/ airport
    # m -> # of edges/connecting flights
    # K -> max number of flights allowed
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