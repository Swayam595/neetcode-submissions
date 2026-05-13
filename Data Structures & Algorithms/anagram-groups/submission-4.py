class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = []
        anagram_dict = dict()

        for word in strs:
            char_dict = [0] * 26

            for char in word:
                i = ord(char) - ord('a')
                char_dict[i] += 1
            
            key_list = []
            for j in range(26):
                key_list.append(str(char_dict[j]))
                key_list.append("#")

            key_str = "".join(key_list)
            
            if key_str not in anagram_dict:
                anagram_dict[key_str] = []
                
            anagram_dict[key_str].append(word)
        
        for key in anagram_dict:
            grouped_anagrams.append(anagram_dict[key])

        return grouped_anagrams