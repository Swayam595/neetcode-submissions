class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # return self.__partition_backtrack(s)
        return self.__partition_dp(s)
    
    # TC -> O(N * 2 ^ N)
    # O(2 ^ N) -> choices we make at each ith position(include current char in partition or extend the range)
    # O(N) -> coping the palindromic substring to ans list
    # SC -> O(N + N ^ 2 + N * 2 ^N) ~ O(N ^ 2 + N * 2 ^ N)
    # O(N) -> recursive stack space
    # O(N ^ 2) -> dp list space
    # O(N * 2 ^ N) -> Output list
    def __partition_dp(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (
                    s[i] == s[i + l - 1] and
                    (
                        i + 1 > (i + l - 2) or
                        dp[i + 1][i + l - 2]
                    )
                )

        ans = []
        self.__partition_dp_dfs(s, 0, [], ans, dp)
        return ans
    
    def __partition_dp_dfs(self, s: str, i: int, part: List[str], ans: List[List[str]], dp:List[List[bool]]) -> None:
        if i >= len(s):
            ans.append(part.copy())
            return
        
        for j in range(i, len(s)):
            if dp[i][j]:
                part.append(s[i : j + 1])
                self.__partition_dp_dfs(s, j + 1, part, ans, dp)
                part.pop()
        return
      
    # TC -> O(N * 2 ^ N)
    # O(2 ^ N) -> choices we make at each ith position(include current char in partition or extend the range)
    # O(N) -> coping the palindromic substring to ans list
    # SC -> O(N + N * 2 ^N)
    # O(N) -> recursive stack space
    # O(N * 2 ^ N) -> Output list
    def __partition_backtrack(self, s: str) -> List[List[str]]:
        ans = []
        self.__partition_backtrack_helper(s, 0, 0, [], ans)
        return ans
    
    def __partition_backtrack_helper(self, s: str, j: int, i: int, part: List[str], ans: List[List[str]]) -> None:
        if i >= len(s):
            if i == j:
                ans.append(part.copy())
            return
        
        if self.__is_palindrome(s, j, i):
            part.append(s[j : i + 1])
            self.__partition_backtrack_helper(s, i + 1, i + 1, part, ans)
            part.pop()
        
        self.__partition_backtrack_helper(s, j, i + 1, part, ans)
        return
    
    def __is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True