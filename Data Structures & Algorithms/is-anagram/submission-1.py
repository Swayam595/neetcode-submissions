class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sCharCountDict = self.__getCharCount(s)
        tCharCountDict = self.__getCharCount(t)

        for char in sCharCountDict:
            if char not in tCharCountDict or sCharCountDict[char] != tCharCountDict[char]:
                return False
        
        return True
        
    def __getCharCount(self, s):
        countDict = dict()

        for char in s:
            if char not in countDict:
                countDict[char] = 0
            countDict[char] += 1
        
        return countDict