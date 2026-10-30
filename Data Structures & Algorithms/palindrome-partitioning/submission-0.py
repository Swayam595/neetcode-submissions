class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.__partition_backtrack1(s)
    
    # TC -> O(N * 2 ^ N)
    # O(2 ^ N) -> choices we make at each ith position 
    # O(N) -> coping the palindromic substring to ans list
    # SC -> O(N + N * 2 ^N)
    # O(N) -> recursive stack space
    # O(N * 2 ^ N) -> Output list
    def __partition_backtrack1(self, s: str) -> List[List[str]]:
        ans = []
        self.__partition_backtrack1_helper(s, 0, 0, [], ans)
        return ans
    
    def __partition_backtrack1_helper(self, s: str, j: int, i: int, part: List[str], ans: List[List[str]]) -> None:
        if i >= len(s):
            if i == j:
                ans.append(part.copy())
            return
        
        if self.__is_palindrome(s, j, i):
            part.append(s[j : i + 1])
            self.__partition_backtrack1_helper(s, i + 1, i + 1, part, ans)
            part.pop()
        
        self.__partition_backtrack1_helper(s, j, i + 1, part, ans)
        return
    
    def __is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True