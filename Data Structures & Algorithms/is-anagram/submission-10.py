class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count = self._get_char_count(s)

        for char in t:
            idx = ord(char) - ord('a')
            s_char_count[idx] -= 1
            if s_char_count[idx] < 0:
                return False
        
        for i in range(26):
            if s_char_count[i] > 0:
                return False
        
        return True
    
    def _get_char_count(self, word):
        char_list = [0] * 26

        for char in word:
            idx = ord(char) - ord('a')
            char_list[idx] += 1
        
        return char_list