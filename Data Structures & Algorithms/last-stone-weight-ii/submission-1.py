class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = stone_sum // 2

        # return self.__recursive(0, stones, 0, target, stone_sum)
        return self.__topDown(stones, stone_sum, target)
    
    def __recursive(self, i: int, stones: List[int], total: int, target: int, stone_sum: int) -> int:
        if total >= target or i == len(stones):
            return abs(total - (stone_sum - total))

        take = self.__recursive(i + 1, stones, total + stones[i], target, stone_sum)
        skip = self.__recursive(i + 1, stones, total, target, stone_sum)

        return min(take, skip)

    def __topDown(self, stones: List[int], stone_sum: int, target: int) -> int:
        N = len(stones)
        memo = [[-1] * (target + 1) for _ in range(N + 1)]
        
        return self.__topDownHelper(0, stones, memo, stone_sum, target, 0)
    
    def __topDownHelper(self, i: int, stones: List[List[int]], memo: List[List[int]], stone_sum: int, target: int, curr_sum: int) -> int:
        if curr_sum >= target or i == len(stones):
            return abs(curr_sum - (stone_sum - curr_sum))

        if memo[i][curr_sum] != -1:
            return memo[i][curr_sum]
        
        take = self.__topDownHelper(i + 1, stones, memo, stone_sum, target, curr_sum + stones[i])
        skip = self.__topDownHelper(i + 1, stones, memo, stone_sum, target, curr_sum)

        memo[i][curr_sum] = min(take, skip)

        return memo[i][curr_sum]
