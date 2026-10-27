class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return self.__generate_parenthesis_brute_force(n)
        # return self.__generate_parenthesis_backtrack(n)
        return self.__generate_parenthesis_dp(n)

    # TC -> O(4^n / √n)
    # Number of valid parentheses strings exist is given by the 
    # Catalan number C_n = (2n)!/(n + 1)! ~ 4^n / √n
    # SC -> O(n)
    def __generate_parenthesis_dp(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                for left in dp[i]:
                    for right in dp[k - i - 1]:
                        dp[k].append("(" + left + ")" + right)
        
        return dp[-1]

    # TC -> O(4^n / √n)
    # Number of valid parentheses strings exist is given by the 
    # Catalan number C_n = (2n)!/(n + 1)! ~ 4^n / √n
    # SC -> O(2n) ~ O(n)
    # Recursion call stack + len of stack
    def __generate_parenthesis_backtrack(self, n: int) -> List[str]:
        ans = []
        stack = []
        self.__backtrack(0, 0, n, stack, ans)
        return ans
    
    def __backtrack(self, open_n: int, close_n: int, n: int, stack: List[str], ans: List[str]) -> None:
        if open_n == close_n == n:
            ans.append("".join(stack))
            return
        
        if open_n < n:
            stack.append("(")
            self.__backtrack(open_n + 1, close_n, n, stack, ans)
            stack.pop()
        
        if close_n < open_n:
            stack.append(")")
            self.__backtrack(open_n, close_n + 1, n, stack, ans)
            stack.pop()

        return
    
    # TC -> O(n * 2^(2 * n))
    # SC -> O(n * 2^(2 * n))
    def __generate_parenthesis_brute_force(self, n: int) -> List[str]:
        ans = []

        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    ans.append(s)
                return

            dfs(s + "(")
            dfs(s + ")")

        def valid(s: str):
            balance = 0
            for c in s:
                balance += 1 if c == '(' else -1
                if balance < 0:
                    return False
            
            return not balance

        dfs("")
        return ans