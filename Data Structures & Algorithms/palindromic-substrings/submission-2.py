class Solution:
    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of input string
    def countSubstrings(self, s: str) -> int:
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