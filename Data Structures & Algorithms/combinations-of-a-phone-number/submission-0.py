class Solution:
    __digit_to_char_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        ans = []
        self.__helper(0, [], digits, ans)
        return ans

    def __helper(self, i, acc, digits, ans):
        if i == len(digits):
            ans.append("".join(acc))
            return
        
        digit = digits[i]
        chars = self.__digit_to_char_map[digit]
        
        for char in chars:
            acc.append(char)
            self.__helper(i + 1, acc, digits, ans)
            acc.pop()

        return  