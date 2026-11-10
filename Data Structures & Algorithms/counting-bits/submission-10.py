class Solution:
    def countBits(self, n: int) -> List[int]:
        # return self.__count_bits_brute_force(n)
        return self.__count_bits_dp(n)

    # TC - O(n)
    # SC -> O(N)      for the output array (O(1) auxiliary)
    # n -> range of number 
    def __count_bits_dp(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == 2 * offset:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
    
    # TC -> O(N * b)  where b = bit-length of n (≈ log₂n)
    # SC -> O(N)      for the output array (O(1) auxiliary)
    def __count_bits_brute_force(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            count = self.__count_bits(i)
            ans.append(count)
        
        return ans

    def __count_bits(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n = n & (n - 1)
        
        return count