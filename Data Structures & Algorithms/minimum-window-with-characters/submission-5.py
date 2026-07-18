class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.__minWindowBruteForce(s, t)
        # return self.__minWindwoSlidingWindow(s, t)
    
    # TC - O(N^2 * M)
    # SC - O(M)
    # N -> len of s
    # M -> len of t
    def __minWindowBruteForce(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(t) == 0:
            return ""

        t_char_space = dict()

        for char in t:
            t_char_space[char] = 1 + t_char_space.get(char, 0)

        ans = [-1, -1]
        min_len = float('inf')

        for l in range(len(s)):
            s_char_space = dict()
            for r in range(l, len(s)):
                s_char_space[s[r]] = 1 + s_char_space.get(s[r], 0)

                if self.__validateMinWindow(t_char_space, s_char_space) and (r - l + 1) < min_len:
                    min_len = r - l + 1
                    ans = [l, r]
        
        l, r = ans

        return s[l : r + 1]

    def __validateMinWindow(self, t_char_space: dict, s_char_space: dict) -> bool:
        for char in t_char_space:
            if t_char_space[char] > s_char_space.get(char, 0):
                return False
        return True

    # TC - O(N * M)
    # SC - O(M)
    # N -> len of s
    # M -> len of t
    def __minWindwoSlidingWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(t) == 0:
            return ""
        ans_index = [-1, -1]
        min_len = float('inf')
        have = 0
        need = len(t)
        t_char_dict = dict()
        for char in t:
            t_char_dict[char] = 1 + t_char_dict.get(char, 0)

        window = dict()
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in t_char_space and window[char] == t_char_space[char]:
                have += 1
            
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans_index = [l, r]
                
                window[s[l]] -= 1
                if s[l] in t_char_space and window[s[l]] < t_char_space[s[l]]:
                    have -= 1
                l += 1
        
        i, j = ans_index
        return s[i : j + 1]