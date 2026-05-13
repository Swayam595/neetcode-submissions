class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.__helper1(1, [], combs, n, k)
        return combs
    
    def __helper1(self, i, acc, combs, n, k):
        if len(acc) == k:
            combs.append(acc.copy())
            return
        
        if i > n:
            return 
        
        acc.append(i)
        self.__helper1(i + 1, acc, combs, n, k)

        acc.pop()
        self.__helper1(i + 1, acc, combs, n, k)
        return
    