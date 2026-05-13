class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagramsDict = dict()

        for s in strs:
            anagram = [0] * 26
            for char in s:
                i = ord(char) - ord('a')
                anagram[i] += 1

            charCount = []
            for count in anagram:
                charCount.append(str(count))
            charCount = ",".join(charCount)
            
            if charCount not in anagramsDict:
                anagramsDict[charCount] = []
            
            anagramsDict[charCount].append(s)
        
        for charCount in anagramsDict:
            ans.append(anagramsDict[charCount])
        
        return ans
        