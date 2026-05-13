class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        # self.__helper1(1, [], combs, n, k)
        self.__helper2(1, [], combs, n, k)
        return combs

    # TC - O(k * 2 ^ n)
    # SC - O(n) + O(k * 2 ^ n) ~ O(k * 2 ^ n)
    def __helper1(self, i: int, acc: List[int], combs: List[List[int]], n: int, k: int) -> None:
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
    
    def __helper2(self, i: int, acc: List[int], combs: List[List[int]], n: int, k: int) -> None:
        if len(acc) == k:
            combs.append(acc.copy())
            return 
        
        if i > n:
            return
        
        for j in range(i, n + 1):
            acc.append(j)
            self.__helper2(j + 1, acc, combs, n, k)
            acc.pop()
        
        return