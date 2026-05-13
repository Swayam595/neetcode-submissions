class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return self.__characterReplacementBruteForce(s, k) # Accepted
        # return self.__characterReplacementSlidingWindow1(s, k) # Accepted
        return self.__characterReplacementSlidingWindow2(s, k) # Accepted

    # TC - O(n^2) SC - O(n)
    def __characterReplacementBruteForce(self, s: str, k: int) -> int:
        max_len = 0
        n = len(s)

        for i in range(n):
            count = dict()
            max_freq = 0
            for j in range(i, n):
                if s[j] not in count:
                    count[s[j]] = 0
                count[s[j]] += 1
                max_freq = max(max_freq, count[s[j]])
                if (j - i + 1) - max_freq <= k:
                    max_len = max(max_len, j - i + 1)
        
        return max_len
    
    # TC - O(n) SC - O(m)
    def __characterReplacementSlidingWindow1(self, s: str, k: int) -> int:
        max_len = 0
        char_set = set(s)

        for c in char_set:
            count = 0
            L = 0
            for R in range(len(s)):
                if s[R] == c:
                    count += 1
                
                while R - L + 1 - count > k:
                    if s[L] == c:
                        count -= 1
                    L += 1
                
                max_len = max(max_len, R - L + 1)
        
        return max_len
    
    # TC - O(n) SC - O(m)
    def __characterReplacementSlidingWindow2(self, s: str, k: int) -> int:
        max_len = 0
        count = dict()

        L = 0
        max_freq = 0

        for R in range(len(s)):
            if s[R] not in count:
                count[s[R]] = 0
            count[s[R]] += 1

            max_freq = max(max_freq, count[s[R]])

            while (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            max_len = max(max_len, R - L + 1)
        
        return max_len
