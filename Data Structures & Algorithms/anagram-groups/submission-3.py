class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagram_dict = dict()

        for word in strs:
            anagram = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                anagram[index] += 1
            
            for i in range(26):
                anagram[i] = str(anagram[i])

            anagram_key = ",".join(anagram)

            if anagram_key not in anagram_dict:
                anagram_dict[anagram_key] = []
            
            anagram_dict[anagram_key].append(word)
        
        return anagram_dict.values()