class Solution:
    # TC -> O(N * Log(N))
    # SC -> O(N)
    # N -> len of stones list
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = self.__create_max(stones)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            if stone1 == stone2:
                continue
            else:
                new_stone = abs(stone1 - stone2)
                heapq.heappush(max_heap, -new_stone)

        return -max_heap[0] if len(max_heap) > 0 else 0

    def __create_max(self, stones: List[int]) -> List[int]:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        return max_heap