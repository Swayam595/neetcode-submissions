class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for char in s:
            if char not in parentheses:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != parentheses[char]:
                    return False
                stack.pop()

        return len(stack) == 0 