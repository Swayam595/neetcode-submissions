class Solution:
    def reverseBits(self, n: int) -> int:
        bits_reversed = 0

        for i in range(32):
            bit = (n >> i) & 1
            bits_reversed = bits_reversed + (bit << (31 - i))
        
        return bits_reversed