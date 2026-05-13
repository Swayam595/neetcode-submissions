class Solution:
    def countBits(self, n: int) -> List[int]:
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