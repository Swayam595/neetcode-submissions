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
            
        # return self.__letter_combinations_recursion(digits)
        return self.__letter_combinations_iteration(digits)

    # TC -> O(N * 4 ^ N)
    # N -> len of digits
    # At each of the N positions we branch up to 4 ways, So the recursion tree has up to 4^N leaves
    # At every leaf you do "".join(acc), which costs O(N)
    # SC -> O(N + N * 4 ^ N)
    # acc buffer: both are at most O(N) deep.
    # Output: there are up to 4^N strings, each of length N
    def __letter_combinations_iteration(self, digits: str) -> List[str]:
        ans = [""]
        for digit in digits:
            acc = []
            for curr_str in ans:
                for c in self.__digit_to_char_map[digit]:
                    acc.append(curr_str + c)
                
            ans = acc
        return ans

    # TC -> O(N * 4 ^ N)
    # N -> len of digits
    # At each of the N positions we branch up to 4 ways, So the recursion tree has up to 4^N leaves
    # At every leaf you do "".join(acc), which costs O(N)
    # SC -> O(N + N * 4 ^ N)
    # Recursion stack + acc buffer: both are at most O(N) deep.
    # Output: there are up to 4^N strings, each of length N
    def __letter_combinations_recursion(self, digits: str) -> List[str]:
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
