class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # return self.__min_window_brute_force(s, t)
        return self.__min_window_optimised(s, t)

    # TC -> O(M + N)
    # SC -> O(K)
    # M -> len of t
    # N -> len of s
    # K -> # of unique chars in s and t
    def __min_window_optimised(self, s: str, t: str) -> str:
        t_char_dict = dict()
        window = dict()

        for char in t:
            t_char_dict[char] = 1 + t_char_dict.get(char, 0)
        
        have = 0
        need = len(t_char_dict)
        res = [-1, -1]
        res_len = float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in t_char_dict and window[char] == t_char_dict[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in t_char_dict and window[s[l]] < t_char_dict[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if res_len != float('inf') else ""

    # TC -> O(M + N ^ 2 * U)
    # SC -> O(K)
    # M -> len of t
    # N -> len of s
    # U -> # of unique chars in t
    # K -> # of unique chars in s and t
    def __min_window_brute_force(self, s: str, t: str) -> str:
        t_char_dict = dict()
        
        for char in t:
            t_char_dict[char] = 1 + t_char_dict.get(char, 0)
                
        n = len(s)
        min_len = float('inf')
        ans = [-1, -1]
        for i in range(n):
            s_char_dict = dict()
            for j in range(i, n):
                s_char_dict[s[j]] = 1 + s_char_dict.get(s[j], 0)

                flag = True
                for char in t_char_dict:
                    if t_char_dict[char] > s_char_dict.get(char, 0):
                        flag = False
                        break
                    
                if flag and (j - i + 1 < min_len):
                    min_len = j - i + 1
                    ans = [i, j]

        l, r = ans
        return s[l: r + 1] if min_len != float('inf') else ""