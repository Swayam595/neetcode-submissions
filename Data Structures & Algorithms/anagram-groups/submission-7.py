class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        ans = []
        for word in strs:
            char_count_array = [0] * 26

            for char in word:
                i = ord(char) -  ord('a')
                char_count_array[i] += 1
            
            anagram_key_array = []
            for i in range(26):
                char = chr(ord('a') + i)
                char_count = char + str(char_count_array[i])
                anagram_key_array.append(char_count)
            
            anagram_key = "".join(anagram_key_array)

            if anagram_key not in anagram_map:
                anagram_map[anagram_key] = []

            anagram_map[anagram_key].append(word)
        

        for key, value in anagram_map.items():
            ans.append(value)
        
        return ans

            
