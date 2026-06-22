class Solution:
    # TC - O(max(N, M))
    # SC - O(max(N, M))
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = self.__getCharMap(s)

        for char in t:
            if char not in char_map:
                return False
            
            char_map[char] -= 1

            if char_map[char] == 0:
                del char_map[char]
            
        return True if len(char_map) == 0 else False

    def __getCharMap(self, s: str):
        char_map = dict()

        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
        
        return char_map