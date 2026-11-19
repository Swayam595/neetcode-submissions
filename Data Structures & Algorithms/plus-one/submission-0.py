class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_rev = digits[::-1]
        carry = 1
        i = 0
        
        while carry and i < len(digits_rev):
            curr_sum = digits_rev[i] + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            digits_rev[i] = digit
            i += 1
        
        if carry:
            digits_rev.append(1)
        
        return digits_rev[::-1]