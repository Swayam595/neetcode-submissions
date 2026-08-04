class Solution:
    def countBits(self, n: int) -> List[int]:
        return self.__count_bits_brute_force(n)

    # TC -> O(n * k)
    # SC -> O(1)
    # n -> range of the number
    # k -> number of set bits in a number
    def __count_bits_brute_force(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            number_of_set_bits = self.__count_set_bits(i)
            ans.append(number_of_set_bits)
        
        return ans
    
    def __count_set_bits(self, n: int) -> int:
        count = 0

        while n > 0:
            count += 1
            n = n & (n - 1)
        
        return count