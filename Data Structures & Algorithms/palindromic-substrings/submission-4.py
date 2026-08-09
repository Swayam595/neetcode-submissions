class Solution:
    def countSubstrings(self, s: str) -> int:
        # return self.__count_substrings_two_pointers(s)
        return self.__count_substrings_manchers(s)

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of input string
    def __count_substrings_manchers(self, s: str) -> int:
        p = self.__manchers(s)
        ans = 0

        for i in p:
            ans += (i + 1) // 2
        
        return ans

    def __manchers(self, s: str) -> List[int]:
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        l, r = 0, 0

        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[l + (r - i)])
            else:
                p[i] = 0

            while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 
                   and t[i + p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1
            
            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]
        
        return p
            
    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of input string
    def __count_substrings_two_pointers(self, s: str) -> int:
        max_palindromes = 0

        for i in range(len(s)):
            max_palindromes += self.__count_palindormeic_sub_strings(i, i, s)
            max_palindromes += self.__count_palindormeic_sub_strings(i, i + 1, s)

        return max_palindromes

    def __count_palindormeic_sub_strings(self, l: int, r: int, s: str) -> int:
        no_of_palindormes = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            no_of_palindormes += 1
            l -= 1
            r += 1
        
        return no_of_palindormes