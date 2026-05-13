class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = dict()

        for i in range(n):
            adj[i] = list()

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        min_heap = []
        for v, w in adj[0]:
            heapq.heappush(min_heap, (w, 0, v))
        
        cost = 0
        visited = set()
        visited.add(0)
    

        while len(min_heap) > 0:
            w, u, v = heapq.heappop(min_heap)
            if v in visited:
                continue

            cost += w
            visited.add(v)

            for neighbor, w in adj[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, v, neighbor))
        if len(visited) == n:
            return cost
        else:
            return -1