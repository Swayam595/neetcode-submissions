class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        return self.__minWindowBruteForce(s, t)
        # return self.__minWindwoSlidingWindow(s, t)
    
    # TC - O(N^2 * M)
    # SC - O(M)
    # N -> len of s
    # M -> len of t
    def __minWindowBruteForce(self, s: str, t: str) -> str:
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

    def __minWindwoSlidingWindow(self, s: str, t: str) -> str:
        l = 0
        char_space = dict()
        ans = ""
        min_len = float('inf')
        len_t = len(t)

        for char in t:
            char_space[char] = 1 + char_space.get(char, 0)
        
        for r in range(len(s)):
            if char in char_space and char_space[char] > 0:
                char_space[char] -= 1
                len_t -= 1
            
            if len_t == 0:
                while l < len(s) and s[l] not in char_space:
                    l += 1
                len_t = len(t)

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]
            
        return ans

