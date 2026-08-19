class Solution:
    # TC -> O(W * N)
    # SC -> O(W)
    # W -> len of words array
    # N -> max len of the word in words array
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagram_dict = dict()

        for word in strs:
            char_count = [0] * 26

            for char in word:
                i = ord(char) - ord('a')
                char_count[i] += 1
            
            anagram_key = self.__build_key(char_count)

            anagram_dict.setdefault(anagram_key, []).append(word)

        for key, values in anagram_dict.items():
            ans.append(values)
        
        return ans

    def __build_key(self, char_count: List[int]) -> str:
        for i in range(26):
            char_count[i] = str(char_count[i])
        
        return "#".join(char_count)