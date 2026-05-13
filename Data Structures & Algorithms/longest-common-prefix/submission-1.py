class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        candidate = strs[0]
        n = len(candidate)
        i = 0

        while i < n:
            for word in strs[1:]:
                if len(word) <= i or candidate[i] != word[i]:
                    return "".join(prefix)
            prefix.append(candidate[i])
            i += 1
        
        return "".join(prefix)
