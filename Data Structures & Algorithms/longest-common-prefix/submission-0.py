class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        first_word = strs[0]

        for i, char in enumerate(first_word):
            char_is_present_in_all_word = True
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    char_is_present_in_all_word = False
                    break
            if char_is_present_in_all_word:
                prefix.append(char)
            else:
                break
        
        return "".join(prefix)