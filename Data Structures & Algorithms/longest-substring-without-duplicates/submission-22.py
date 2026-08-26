class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return self.__length_of_longest_substring_brute_force(s)
        return self.__length_of_longest_substring_optimised(s)

    # TC -> O(N ^ 2)
    # SC -> O(N)
    # N -> len of s
    def __length_of_longest_substring_optimised(self, s: str) -> int:
        char_last_seen_at = dict()
        max_len = 0
        n = len(s)
        curr_len = 0
        window_start = 0

        for i in range(n):
            char = s[i]
            if char in char_last_seen_at:
                window_start = max(window_start, char_last_seen_at[char] + 1)

            char_last_seen_at[char] = i
            curr_len = i - window_start + 1
            max_len = max(max_len, curr_len)
        
        return max_len


    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of s
    def __length_of_longest_substring_brute_force(self, s: str) -> int:
        max_len = 0
        n = len(s)

        for i, char in enumerate(s):
            curr_window = 1
            for j in range(i + 1, n):
                if char == s[j]:
                    max_len = max(max_len, curr_window)
                    break
                curr_window += 1
        
        return max_len