class Solution:
    def hammingWeight(self, n: int) -> int:
        # return self.__getHammingWeight(n) # Accepted
        return self.__getHammingWeightOptimized(n)
    
    # TC - O(log(n)) SC - O(1)
    def __getHammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        
        return count
    
    # TC - O(k) SC - O(1)
    # where k = numbder of set bits
    def __getHammingWeightOptimized(self, n: int) -> int:
        count = 0

        while n > 0:
            count += 1
            n = n & (n - 1)
        
        return count
