class Solution:
    def countBits(self, n: int) -> List[int]:
        # return self.__countBitsBruteForce(n) # Accepted
        return self.__countBitsOptimizedDp(n)

    # TC - O(n * m) SC - O(1)
    # where n is the range 
    # and m is the number of set bits in a number 
    def __countBitsBruteForce(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            set_bits = self.__getHammingDistance(i)
            ans.append(set_bits)
        
        return ans
        
    def __getHammingDistance(self, m: int) -> int:
        count = 0

        while m > 0:
            count += 1
            m = m & (m - 1)
        
        return count
    
    def __countBitsOptimizedDp(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp