class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = self.__createEdges(points)
        adj = dict()
        cost = 0
        min_heap = []
        visited = set()
        
        for x, y in points:
            adj[(x, y)] = list()
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        x, y = points[0]

        for v, w in adj[(x, y)]:
            heapq.heappush(min_heap, (w, (x, y), v))
        
        visited.add((x, y))

        while len(min_heap) > 0:
            w1, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue
            
            visited.add(v)
            cost += w1

            for neighbor, w2 in adj[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w2, v, neighbor))

        return cost
    
    def __createEdges(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                weight = abs(x2 - x1) + abs(y2 - y1)
                edges.append([(x1, y1), (x2, y2), weight])
        
        return edges