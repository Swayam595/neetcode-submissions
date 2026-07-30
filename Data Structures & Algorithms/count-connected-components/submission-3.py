class Sets:
    def __init__(self, n: int):
        self.__n = n
        self.__parent = {i: i for i in range(n)}
        self.__rank = {i: 1 for i in range(n)}
        self.__connected_components = n
    
    # TC - O(α(N))
    # SC - O(1)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # n - Number of nodes 
    def find(self, x: int) -> int:
        parent = self.__parent[x]

        while self.__parent[parent] != parent:
            self.__parent[parent] = self.__parent[self.__parent[parent]]
            parent = self.__parent[parent]
        
        return parent

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
            self.__parent[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        else:
            self.__parent[p1] = p2
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
        