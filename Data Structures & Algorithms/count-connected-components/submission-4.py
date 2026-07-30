class Sets:
    def __init__(self, n: int):
        self.__parents = dict()
        self.__rank = dict()
        self.__connected_components = n

        for i in range(n):
            self.__parents[i] = i
            self.__rank[i] = 1

    # TC - O(α(N))
    # SC - O(1)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # N - Number of node
    def find(self, x: int) -> int:
        p = self.__parents[x]

        while p != self.__parents[p]:
            self.__parents[p] = self.__parents[self.__parents[p]]
            p = self.__parents[p]
        
        return p
    
    # TC - O(α(N))
    # SC - O(1)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # N - Number of nodes
    def union(self, u: int, v: int) -> None:
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return 
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parents[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        else:
            self.__parents[p1] = p2
            self.__rank[p2] += self.__rank[p1]
        
        self.__connected_components -= 1
        return
    
    # TC - O(1) SC - O(1)
    def getConnectedComponents(self) -> int:
        return self.__connected_components

class Solution:
    # TC - O(N + M * α(N))
    # SC - O(N)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # N - Number of nodes 
    # M - len of edges
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        sets = Sets(n)

        for u, v in edges:
            sets.union(u, v)

        return sets.getConnectedComponents()
        