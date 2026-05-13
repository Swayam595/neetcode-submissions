class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        first_word = strs[0]
        n = len(first_word)

        for i, char in enumerate(first_word):
            for word in strs[1:]:
                if len(word) <= i or char != word[i]:
                    return "".join(prefix)

            prefix.append(char)
        
        return "".join(prefix)
