class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        char_count_of_s = self.__get_char_count_of_s(s)

        for char in t:
            if char in char_count_of_s and char_count_of_s[char] > 0:
                char_count_of_s[char] -= 1
            else:
                return False
        
        return True

    
    def __get_char_count_of_s(self, s):
        char_count = dict()

        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        return char_count