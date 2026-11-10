class Solution:
    def countBits(self, n: int) -> List[int]:
        return self.__count_bits_brute_force(n)
    
    # TC -> O(N * M)
    # SC -> O(1)
    # N -> Given integer n
    # M -> # of bits in a num which lie in the range (0, n)
    def __count_bits_brute_force(self, n: int) -> List[int]:
        ans = [0]

        for i in range(1, n + 1):
            count = self.__count_bits(i)
            ans.append(count)
        
        return ans

    def __count_bits(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        
        return count