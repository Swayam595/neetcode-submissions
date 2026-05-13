class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        total_weight = 0
        components =n
        min_heap = []
        union_find = UnionFind(n)

        for n1, n2, weight in edges:
            heapq.heappush(min_heap, (weight, n1, n2))
        
        while len(min_heap) > 0 and components > 1:
            weight, n1, n2 = heapq.heappop(min_heap)

            if not union_find.union(n1, n2):
                continue
            
            components -= 1
            total_weight += weight
        
        return total_weight if components == 1 else -1

class UnionFind:
    def __init__(self, n: int) -> None:
        self.__parent = dict()
        self.__rank = dict()

        for i in range(n):
            self.__parent[i] = i
            self.__rank[i] = 0
    
    def union(self, n1: int, n2: int) -> bool:
        p1 = self.__find(n1)
        p2 = self.__find(n2)

        if p1 == p2:
            return False

        if self.__rank[p1] > self.__rank[p2]:
            self.__parent[p2] = p1
        else:
            self.__parent[p1] = p2
            self.__rank[p2] += 1
        
        return True
    
    def __find(self, n: int) -> int:
        p = self.__parent[n]

        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]
            p = self.__parent[p]
        
        return p