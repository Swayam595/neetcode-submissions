class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return self.__longest_palindrome_two_pointers(s)
        return self.__longest_palindrome_manchers(s)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of the input string
    def __longest_palindrome_manchers(self, s: str) -> str:
        p = self.__mancher(s)
        res_len, center_idx = max((v, i ) for i, v in enumerate(p))
        res_idx = (center_idx - res_len) // 2
        return s[res_idx: res_idx + res_len]

    def __mancher(self, s: str) -> List[int]:
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        l, r = 0, 0

        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[l + (r - i)])
            else:
                p[i] = 0

            while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1
            
            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]
        
        return p

    # TC -> O(N ^ 2)
    # SC -> O(N)
    # N -> len of the input string
    def __longest_palindrome_two_pointers(self, s: str) -> str:
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