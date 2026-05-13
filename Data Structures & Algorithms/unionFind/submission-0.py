class UnionFind:
    
    def __init__(self, n: int):
        self.__par = dict()
        self.__rank = dict()

        for i in range(n):
            self.__par[i] = i
            self.__rank[i] = 0
        

    def find(self, x: int) -> int:
        p = self.__par[x]
        while p != self.__par[p]:
            self.__par[p] = self.__par[self.__par[p]]
            p = self.__par[p]
        return p
        

    def isSameComponent(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        return p1 == p2


    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 == p2:
            return False
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__par[p2] = p1
        elif self.__rank[p1] < self.__rank[p2]:
            self.__par[p1] = p2
        else:
            self.__par[p1] = p2
            self.__rank[p2] += 1
        
        return True

    def getNumComponents(self) -> int:
        count = 0
        for node in self.__par:
            if node == self.__par[node]:
                count += 1
        
        return count

