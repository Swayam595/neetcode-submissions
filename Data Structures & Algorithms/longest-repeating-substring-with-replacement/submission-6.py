class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return self.__characterReplacementBruteForce(s, k)
        # return self.__characterReplacementSlidingWindow(s, k)
        return self.__characterReplacementSlidingWindowOptmial(s, k)


    def __characterReplacementBruteForce(self, s: str, k: int) -> int:
        max_len = 0

        for i in range(len(s)):
            count = dict()
            curr_len = 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                curr_len = max(curr_len, count[s[j]])
                if (j - i + 1) - curr_len <= k:
                    max_len = max(max_len, j - i + 1)
        
        return max_len
    
    def __characterReplacementSlidingWindow(self, s: str, k: int) -> int:
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
    
    def __characterReplacementSlidingWindowOptmial(self, s: str, k: int) -> int:
        count = dict()
        max_len = 0

        l = 0
        curr_len = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            curr_len = max(curr_len, count[s[r]])

            while r - l + 1 - curr_len > k:
                count[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len