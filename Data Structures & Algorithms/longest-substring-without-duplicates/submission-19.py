class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return self.__lengthOfLongestSubstringBruteForce(s)
        return self.__lengthOfLongestSubstringSlidingWindow(s)
    
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
    
    def __lengthOfLongestSubstringSlidingWindow(self, s: str) -> int:
        if len(s) == 0:
            return 0

        last_seen_at = dict()
        max_len = 1
        l = 0

        for r, char in enumerate(s):
            if char in last_seen_at:
                l = max(last_seen_at[char] + 1, l)

            max_len = max(max_len, r - l + 1)
            last_seen_at[char] = r
            
        return max_len