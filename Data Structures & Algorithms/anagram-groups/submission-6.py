class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        groups_dict = dict()

        for word in strs:
            char_hash_list = ['0'] * 26

            for char in word:
                idx = ord(char) - ord('a')
                count = int(char_hash_list[idx]) + 1
                char_hash_list[idx] = str(count)
            
            char_hash = "#".join(char_hash_list)

            if char_hash not in groups_dict:
                groups_dict[char_hash] = []
            
            groups_dict[char_hash].append(word)
        

        for char_hash in groups_dict:
            words = groups_dict[char_hash]
            groups.append(words)
        
        return groups