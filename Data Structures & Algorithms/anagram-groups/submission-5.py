class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = []
        anagram_dict = dict()

        for word in strs:
            char_dict = ['0'] * 26

            for char in word:
                i = ord(char) - ord('a')
                count = int(char_dict[i]) + 1
                char_dict[i] = str(count)

            key_str = "#".join(char_dict)
            
            if key_str not in anagram_dict:
                anagram_dict[key_str] = []
                
            anagram_dict[key_str].append(word)
        
        for key in anagram_dict:
            grouped_anagrams.append(anagram_dict[key])

        return grouped_anagrams