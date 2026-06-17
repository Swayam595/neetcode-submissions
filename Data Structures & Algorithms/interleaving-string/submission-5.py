class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:        
        # return self.__recursive(s1, s2, s3, 0, 0, 0)
        return self.__topDown(s1, s2, s3)
    
    # TC -> O(2 ^ (K))
    # SC -> O(K)
    def __recursive(self, s1: str, s2: str, s3: str, i: int, j: int, k: int) -> bool:
        if k == len(s3):
            return i == len(s1) and j == len(s2)
        
        if i < len(s1) and s1[i] == s3[k]:
            return self.__recursive(s1, s2, s3, i + 1, j, k + 1)
        
        if j < len(s2) and s2[j] == s3[k]:
            return self.__recursive(s1, s2, s3, i, j + 1, k + 1)

        return False

    # TC -> O(N * M)
    # SC -> O(N * M)
    def __topDown(self, s1: str, s2: str, s3: str) -> bool:   
        N = len(s1)
        M = len(s2)

        if N + M != len(s3):
            return False

        memo = [[None] * (M + 1) for _ in range(N + 1)]

        return self.__topDownHelper(s1, s2, s3, 0, 0, 0, memo)
    
    # TC -> O(N * M)
    # SC -> O(N + M)
    def __topDownHelper(self, s1: str, s2: str, s3: str, 
                              i: int, j: int, k: int, memo: List[List[int]]) -> bool:
        if k == len(s3):
            return i == len(s1) and j == len(s2)
        
        if memo[i][j] != None:
            return memo[i][j]
        
        res = False
        if i < len(s1) and s1[i] == s3[k]:
            res = self.__topDownHelper(s1, s2, s3, i + 1, j, k + 1, memo)

        if not res and j < len(s2) and s2[j] == s3[k]:
            res = self.__topDownHelper(s1, s2, s3, i, j + 1, k + 1, memo)
        
        memo[i][j] = res
        return memo[i][j]