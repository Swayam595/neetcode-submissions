class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            char1 = s[l]
            char2 = s[r]

            if not self.__isAlphaNumeric(char1):
                l += 1
            elif not self.__isAlphaNumeric(char2):
                r -= 1
            elif char1.lower() != char2.lower():
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def __isAlphaNumeric(self, char) -> bool:
        return ('A' <= char <= 'Z' or
                'a' <= char <= 'z' or
                '0' <= char <= '9')