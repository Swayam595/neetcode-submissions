class Solution:
    # TC -> O(N ^ 2 + 2M + N * log(M)) ~ O(N ^ 2 + N * log(M)) ~ O(N ^ 2)
    # SC -> O(N ^ 2)
    # N -> len of points
    # M -> # of edges ~ O(N ^ 2)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = self.__get_manhattan_distance(points)
        adj_dict = self.__get_adj_dict(dist, points)

        return self.__comute_cost(points[0], adj_dict)
    
    # TC -> O(M + N * log(M))
    # SC -> O(M)
    # N -> len of points
    # M -> # of edges ~ O(N ^ 2)
    def __comute_cost(self, src: List[int], adj_dict: dict[tuple[int], List[tuple]]) -> int:
        cost = 0
        min_heap = list()
        visited = set()

        x, y = src
        for v, w in adj_dict[(x, y)]:
            heapq.heappush(min_heap, (w, v))
        visited.add((x, y))

        while len(min_heap) > 0:
            w1, v1 = heapq.heappop(min_heap)
            if v1 in visited:
                continue
            
            cost += w1
            visited.add(v1)

            for v2, w2 in adj_dict[v1]:
                if v2 not in visited:
                    heapq.heappush(min_heap, (w2, v2))
        
        return cost

    # TC -> O(N + M) ~ O(M)
    # SC -> O(M)
    # N -> len of points
    # M -> # of edges ~ O(N ^ 2)
    def __get_adj_dict(self, edges: List[tuple], points: List[List[int]]) -> dict[tuple[int], List[tuple]]:
        adj_dict = {(x, y): list() for x, y in points}

        for u, v, w in edges:
            adj_dict[u].append((v, w))
            adj_dict[v].append((u, w))
        
        return adj_dict

    # TC -> O(N ^ 2)
    # SC -> O(N ^ 2)
    # N -> len of points
    def __get_manhattan_distance(self, points: List[List[int]]) -> List[tuple]:
        manhattan_distance = list()
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                manhattan_distance.append(
                    (
                        (x1, y1),
                        (x2, y2),
                        dist
                    )
                )
        return manhattan_distance