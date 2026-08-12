class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.__recursive(0, s, wordDict)
        # return self.__top_down(s, wordDict)
        return self.__bottom_up(s, wordDict)
        
    # TC -> O(N * M * t)
    # SC -> O(N)
    # N -> len of s
    # M -> len of word dict
    # t -> max len of the word in word dict
    def __bottom_up(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if i + word_len <= n and s[i : i + word_len] == word:
                    if dp[i + word_len]:
                        dp[i] = True
        
        return dp[0]

    def __top_down(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * len(s)

        return self.__top_down_helper(0, s, wordDict, cache)
    
    # TC -> O(N * M * t)
    # SC -> O(N)
    # N -> len of s
    # M -> len of word dict
    # t -> max len of the word in word dict
    def __top_down_helper(self, i: int, s: str, word_dict: List[str], cache: List[bool]) -> bool:
        if i >= len(s):
            return True
        
        if cache[i]:
            return cache[i]

        
        for word in word_dict:
            word_len = len(word)
            if i + word_len <= len(s) and s[i : i + word_len] == word:
                if self.__top_down_helper(i + word_len, s, word_dict, cache):
                    cache[i] = True
                    return cache[i]
        
        return False
    
    # TC -> O(t * (M ^ N))
    # SC -> O(N)
    # M -> len of wordDict
    # N -> len of s
    # t -> max len of any word wordDict
    def __recursive(self, i: int, s: str, word_dict: List[str]) -> bool:
        if i >= len(s):
            return True
            
        for word in word_dict:
            word_len = len(word)
            if i + word_len <= len(s) and s[i : i + word_len] == word:
                if self.__recursive(i + word_len, s, word_dict):
                    return True
        
        return False