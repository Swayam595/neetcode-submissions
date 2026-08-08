class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans = ""

        for i in range(len(s)):
            palindrome = self.__find_palindrome(i, i, s)
            if len(palindrome) > max_len:
                max_len = len(palindrome)
                ans = palindrome

            palindrome = self.__find_palindrome(i, i + 1, s)
            if len(palindrome) > max_len:
                max_len = len(palindrome)
                ans = palindrome
        
        return ans
    
    def __find_palindrome(self, l: int, r: int, s: str) -> str:
        palindorme = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindorme = s[l : r + 1]
            l -= 1
            r += 1

        return palindorme