class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.__lengthOfLongestSubstringBruteForce(s)
    
    def __lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        max_len = 0
        for i, curr_char in enumerate(s):
            curr_char_set = set(curr_char)
            for char in s[i + 1:]:
                if char in curr_char_set:
                    break
                curr_char_set.add(char)
            
            max_len = max(max_len, len(curr_char_set))
            
        return max_len