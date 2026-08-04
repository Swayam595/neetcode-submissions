class Solution:
    def countBits(self, n: int) -> List[int]:
        # return self.__count_bits_brute_force(n)
        return self.__count_bits_dp(n)

    # TC - O(n)
    # SC -> O(1)
    # n -> range of number 
    def __count_bits_dp(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == 2 * offset:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

    # TC -> O(n * k)
    # SC -> O(1)
    # n -> range of the number
    # k -> number of set bits in a given number bounded by logn
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