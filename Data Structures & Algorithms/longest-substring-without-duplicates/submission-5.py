class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.__lengthOfLongestSubstringBruteForce(s)
    
    # TC - O(n * m) SC - O(m) 
    def __lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        max_len = 0
        n = len(s)
        for i in range(n):
            char_set = set()
            for j in range(i, n):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            max_len = max(max_len, len(char_set))
        
        return max_len