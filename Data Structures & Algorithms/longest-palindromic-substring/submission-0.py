class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l = 0
        max_r = 0
        max_length = 0
        N = len(s)

        for i in range(N):
            odd_l, odd_r, odd_length = self.__findLongestPalindrome(i, i, s)
            even_l, even_r, even_length = self.__findLongestPalindrome(i, i + 1, s)

            if even_length > odd_length and even_length > max_length:
                max_l = even_l
                max_r = even_r
                max_length = even_length
            elif even_length < odd_length and odd_length > max_length:
                max_l = odd_l
                max_r = odd_r
                max_length = odd_length
        
        return s[max_l: max_r + 1]
    
    def __findLongestPalindrome(self, l: int, r: int, s: str) -> Tuple:
        length = 0
        max_l = l
        max_r = r

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > length:
                length = r - l + 1
                max_l = l
                max_r = r
            l -= 1
            r += 1
        
        return max_l, max_r, length
