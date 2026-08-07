class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            curr_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2

            if curr_bit:
                ans = ans | (1 << i)
            
        if ans > 0x7FFFFFFF:
            ans = ~(ans ^ mask)
        
        return ans