class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            while l < r and not self.__validate_char(s[l]):
                l += 1
            
            while l < r and not self.__validate_char(s[r]):
                r -= 1
            
            if l <= r and s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True

    def __validate_char(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord('z')
                or ord('A') <= ord(s) <= ord('Z')
                or ord('0') <= ord(s) <= ord('9'))