class Solution:
    # TC -> O(N)
    # SC -> O(M)
    # N -> len of tokens
    # M -> # Ints in the tokens
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"

        for char in tokens:
            if char in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                num = self.__perform_operations(num1, num2, char)
            else:
                num = int(char)
            stack.append(num)
        
        return stack[0]


    def __perform_operations(self, num1: int, num2: int, operator: chr) -> int:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        else:
            return int(num1 / num2)
