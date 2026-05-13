class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {"}": "{", ")": "(", "]": "["}

        for i in s:
            if i not in bracket_dict:
                stack.append(i)
            else:
                if len(stack) == 0 or stack[-1] != bracket_dict[i]:
                    return False
                stack.pop()
        
        return len(stack) == 0