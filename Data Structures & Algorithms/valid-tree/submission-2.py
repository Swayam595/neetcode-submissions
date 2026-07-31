class Sets:
    def __init__(self, n: int) -> None:
        self.__connected_components = n
        self.__parents = dict()
        self.__rank = dict()

        for i in range(n):
            self.__parents[i] = i
            self.__rank[i] = 1
    
    # TC -> O(α(n))
    # SC -> O(1)
    # α(n) -> inverse Ackermann function (essentially constant)
    # n -> # of nodes
    def find(self, x: int) -> int:
        p = self.__parents[x]

        while p != self.__parents[p]:
            self.__parents[p] = self.__parents[self.__parents[p]]
            p = self.__parents[p]

        return p
    
    # TC -> O(α(n))
    # SC -> O(1)
    # α(n) -> inverse Ackermann function (essentially constant)
    # n -> # of nodes
    def union(self, u: int, v: int) -> bool:
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return True

        if self.__rank[p1] > self.__rank[p2]:
            self.__parents[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        else:
            self.__parents[p1] = p2
            self.__rank[p2] += self.__rank[p1]
        
        self.__connected_components -= 1

        return False
    
    # TC -> O(1) 
    # SC -> O(1)
    def getConnectedComponents(self) -> int:
        return self.__connected_components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.__validTreeUsingUnionFind(n, edges)

    # TC - O(E * α(n))
    # SC - O(n)
    # α(n) -> inverse Ackermann function (essentially constant)
    # E -> # of edges
    # n -> # of nodes
    def __validTreeUsingUnionFind(self, n: int, edges: List[List[int]]) -> bool:
        sets = Sets(n)

        for u, v in edges:
            if sets.union(u, v):
                return False
        
        return sets.getConnectedComponents() == 1
