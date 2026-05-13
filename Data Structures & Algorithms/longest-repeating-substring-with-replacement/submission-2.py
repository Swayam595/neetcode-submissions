class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.__characterReplacementBruteForce(s, k)

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