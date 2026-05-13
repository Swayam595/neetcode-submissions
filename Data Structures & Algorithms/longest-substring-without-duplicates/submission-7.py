class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return self.__lengthOfLongestSubstringBruteForce(s) # Accepted
        # return self.__lengthOfLongestSubstringSlidingWindow1(s) # Accepted
        return self.__lengthOfLongestSubstringSlidingWindow2(s) # Accepted
    
    # TC - O(n^2) SC - O(n) 
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
    
    # TC - O(n) SC - O(m)
    def __lengthOfLongestSubstringSlidingWindow1(self, s: str) -> int:
        window = set()
        L = 0
        max_len = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            
            window.add(s[R])
            max_len = max(max_len, R - L + 1)
        
        return max_len
    
    # TC - O(n) SC - O(m)
    def __lengthOfLongestSubstringSlidingWindow2(self, s: str) -> int:
        max_len = 0

        char_dict = dict()
        L = 0

        for R in range(len(s)):
            if s[R] in char_dict:
               L = max(char_dict[s[R]] + 1, L)
            char_dict[s[R]] = R
            max_len = max(max_len, R - L + 1)
        
        return max_len
        