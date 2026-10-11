class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.__climb_stairs_recursive(n)
        # return self.__climb_stairs_bottom_up(n)
        # return self.__climb_stairs_top_down(n)
        return self.__climb_stairs_top_down_optimised(n)
    
    # TC -> O(N)
    # SC -> O(1)
    # N -> is the integer n
    def __climb_stairs_top_down_optimised(self, n: int) -> int:
        if n <= 2:
            return n

        take_1_step = 1
        take_2_step = 2
        
        for i in range(3, n + 1):
            take_3_step = take_1_step + take_2_step
            take_1_step = take_2_step
            take_2_step = take_3_step
        
        return take_2_step

    # TC -> O(N)
    # SC -> O(N) -> len of the dp array
    # N -> is the integer n
    def __climb_stairs_top_down(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i <= 2:
                dp[i] = i
            else:
                take_1_step = dp[i - 1]
                take_2_step = dp[i - 2]
                dp[i] = take_1_step + take_2_step
        
        return dp[n]

    # TC -> O(N)
    # SC -> O(2N) ~ O(N) -> len of the recursive stack and memo array len
    # N -> is the integer n
    def __climb_stairs_bottom_up(self, n: int) -> int:
        memo = [0] * (n + 1)

        return self.__climb_stairs_bottom_up_helper(n, memo)

    def __climb_stairs_bottom_up_helper(self, n: int, memo: list[int]) -> int:
        if n <= 2:
            return n
        
        if memo[n] != 0:
            return memo[n]
        take_1_step = self.__climb_stairs_bottom_up_helper(n - 1, memo)
        take_2_step = self.__climb_stairs_bottom_up_helper(n - 2, memo)

        memo[n] = take_1_step + take_2_step

        return memo[n]
         
    
    # TC -> O(2 ^ N)
    # SC -> O(N) ~ len of the recursive stack
    # N -> is the integer n
    def __climb_stairs_recursive(self, n: int) -> int:
        if n <= 2:
            return n
        
        take_1_step = self.__climb_stairs_recursive(n - 1)
        take_2_step = self.__climb_stairs_recursive(n - 2)

        return take_1_step + take_2_step