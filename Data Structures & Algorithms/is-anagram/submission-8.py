class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_of_s = self.__get_char_count_of_string(s)

        for char in t:
            j = self.__get_char_index_in_dict(char)
            char_count_of_s[j] -= 1
            if char_count_of_s[j] < 0:
                return False
        
        for k in range(26):
            if char_count_of_s[k] > 0:
                return False
        
        return True
    
    def __get_char_count_of_string(self, string):
        char_count_dict = [0] * 26

        for char in string:
            i = self.__get_char_index_in_dict(char)
            char_count_dict[i] += 1
        
        return char_count_dict
    
    def __get_char_index_in_dict(self, char):
        return ord(char) - ord('a')

