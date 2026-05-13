class Sets:
    def __init__(self, n: int) -> None:
        self.__parent = dict()
        self.__rank = dict()
        self.__number_of_connected_components = n

        for i in range(n):
            self.__parent[i] = i
            self.__rank[i] = 0
        
    def find(self, x: int) -> int:
        p = self.__parent[x]

        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]
            p = self.__parent[p]
        
        return p
    
    def union(self, x: int, y: int) -> None:
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 == p2:
            return
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parent[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        elif self.__rank[p1] < self.__rank[p2]:
            self.__parent[p1] = p2
            self.__rank[p2] += self.__rank[p1]
        else:
            self.__parent[p1] = p2
            self.__rank[p2] += 1
        self.__number_of_connected_components -= 1
        return
    
    def get_number_of_connected_components(self) -> int:
        return self.__number_of_connected_components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        sets = Sets(n)

        for x, y in edges:
            sets.union(x, y)
        
        return sets.get_number_of_connected_components()
        