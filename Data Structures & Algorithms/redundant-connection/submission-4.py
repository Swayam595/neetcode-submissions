class Sets:
    def __init__(self, n: int):
        self.__parent = dict()
        self.__rank = dict()

        for i in range(1, n + 1):
            self.__parent[i] = i
            self.__rank[i] = 1
        
    def find(self, x: int) -> int:
        p = self.__parent[x]

        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]
            p = self.__parent[p]

        return p 
    
    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 == p2:
            return False
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parent[p2] = p1
            # self.__rank[p1] += self.__rank[p2]
        elif self.__rank[p1] < self.__rank[p2]:
            self.__parent[p1] = p2
        else:
            self.__parent[p1] = p2
            self.__rank[p2] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        sets = Sets(n)
        ans = []

        for x, y in edges:
            if not sets.union(x, y):
                ans = [x, y]
        
        return ans