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
        self.__back_track(0, digits, [], ans)
        return ans

    def __back_track(self, i: int, digits: str, acc: List[str], ans: List[str]) -> None:
        if i >= len(digits):
            ans.append("".join(acc))
            return
        
        digit = digits[i]
        for char in self.__digit_to_char_map[digit]:
            acc.append(char)
            self.__back_track(i + 1, digits, acc, ans)
            acc.pop()
        
        return
