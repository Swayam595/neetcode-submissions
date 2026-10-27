class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.__generate_parenthesis_brute_force(n)
    
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