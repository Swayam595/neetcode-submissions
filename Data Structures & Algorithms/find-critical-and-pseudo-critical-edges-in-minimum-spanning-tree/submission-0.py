class UnionFind:
    def __init__(self, n):
        self.__parent = [i for i in range(n)]
        self.__rank = [1] * n
        self.max_rank = 0
    
    def find(self, v):
        while v != self.__parent[v]:
            self.__parent[v] = self.__parent[self.__parent[v]]
            v = self.__parent[v]
        
        return v
    
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)

        if p1 == p2:
            return False
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parent[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        else:
            self.__parent[p1] = p2
            self.__rank[p2] += self.__rank[p1]
        
        self.max_rank = max(self.max_rank, self.__rank[p1], self.__rank[p2])

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key = lambda x: x[2])

        uf = UnionFind(n)
        mst_weight = 0

        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
            
        critical = []
        pseudo = []

        for u1, u2, e_weight, i in edges:
            uf = UnionFind(n)
            weight = 0

            for x1, x2, w, j in edges:
                if i != j and uf.union(x1, x2):
                    weight += w
            
            if uf.max_rank != n or weight > mst_weight:
                critical.append(i)
                continue
            
            uf = UnionFind(n)
            uf.union(u1, u2)
            weight = e_weight

            for v1, v2, w, k in edges:
                if uf.union(v1, v2):
                    weight += w
            
            if weight == mst_weight:
                pseudo.append(i)
            
        return [critical, pseudo]
            
