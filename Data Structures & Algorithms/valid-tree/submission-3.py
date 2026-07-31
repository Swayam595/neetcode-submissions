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
        return self.__validTreeUsingDfs(n, edges)
        # return self.__validTreeUsingUnionFind(n, edges)

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

    def __validTreeUsingDfs(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj_dict = {i: [] for i in range(n)}
        for u, v in edges:
            adj_dict[u].append(v)
            adj_dict[v].append(u)

        visited = set()

        return self.__dfs(0, -1, adj_dict, visited) and len(visited) == n
    
    def __dfs(self, node: int, parent: int, adj_dict: dict, visited: set) -> bool:
        if node in visited:
            return False
        
        visited.add(node)

        for neighbor in adj_dict[node]:
            if neighbor == parent:
                continue
            
            if not self.__dfs(neighbor, node, adj_dict, visited):
                return False
            
        return True
