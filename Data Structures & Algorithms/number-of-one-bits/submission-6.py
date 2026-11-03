class Solution:
    def hammingWeight(self, n: int) -> int:
        # return self.__get_hamming_distance(n)
        return self.__get_hamming_distance_optimised(n)
    
    # TC -> O(log(n)) ~ O(b)
    # SC -> O(1)
    # b -> # of bits i.e. 32
    def __get_hamming_distance(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1
        
        return count

    # TC -> O(k)
    # k -> # of set bits
    def __get_hamming_distance_optimised(self, n: int) -> int:
        count = 0

        while n > 0:
            count += 1
            n = n & (n - 1)

        return count