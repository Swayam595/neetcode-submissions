class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return self.__character_replacement_brute_force(s, k)
        # return self.__character_replacement_sliding_window(s, k)
        return self.__character_replacement_sliding_window_optimised(s, k)

    # TC -> O(N)
    # SC -> O(1)
    # N -> Len of s
    def __character_replacement_sliding_window_optimised(self, s: str, k: int) -> int:
        count = dict()
        max_len = 0

        l = 0
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len

    # TC -> O(N)
    # SC -> O(1)
    # N -> Len of s
    def __character_replacement_sliding_window(self, s: str, k: int) -> int:
        unique_chars = set()
        max_len = 0
        for char in s:
            unique_chars.add(char)

        for char in unique_chars:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                
                while r - l + 1 - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                
                max_len = max(max_len, r - l + 1)
        
        return max_len

    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> Len of s
    def __character_replacement_brute_force(self, s: str, k: int) -> int:
        max_len = 0
        
        for i, char in enumerate(s):
            replacement_remaining = k
            curr_len = 1
            for j in range(i + 1, len(s)):
                if char == s[j]:
                    curr_len += 1
                elif replacement_remaining > 0:
                    replacement_remaining -= 1
                    curr_len += 1
                else:
                    break
                max_len = max(max_len, curr_len)
        
        return max_len
