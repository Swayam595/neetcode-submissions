class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.__getHammingWeight(n)
    
    def __getHammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        
        return count