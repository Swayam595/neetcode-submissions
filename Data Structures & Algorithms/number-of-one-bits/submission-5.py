class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.__get_hamming_distance(n)
    
    def __get_hamming_distance(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1
        
        return count