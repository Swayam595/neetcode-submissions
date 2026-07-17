class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1

        while i < j:
            while i < j and not self.checkAlphaNum(s[i]):
                i += 1
            
            while i < j and not self.checkAlphaNum(s[j]):
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        
        return True
    
    def checkAlphaNum(self, char: chr) -> bool:
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )