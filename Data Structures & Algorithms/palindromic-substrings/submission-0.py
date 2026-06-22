class Solution:
    def countSubstrings(self, s: str) -> int:
        max_palindromes = 0
        N = len(s)

        for i in range(N):
           max_palindromes += self.__findLongestPalindrome(i, i, s)
           max_palindromes += self.__findLongestPalindrome(i, i + 1, s)

        return max_palindromes
    
    def __findLongestPalindrome(self, l: int, r: int, s: str) -> int:
        no_of_palindromes = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            no_of_palindromes += 1
            l -= 1
            r += 1
        
        return no_of_palindromes
