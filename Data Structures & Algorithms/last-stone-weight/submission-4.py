class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # return self.__last_stone_weight_heap(stones)
        return self.__last_stone_weight_bucket_sort(stones)

    # TC -> O(N + W)
    # SC -> O(W)
    # N -> len of stones list
    # W -> Max stone size in the stones list
    def __last_stone_weight_bucket_sort(self, stones: List[int]) -> int:
        max_stone = max(stones)
        bucket = [0] * (max_stone + 1)

        for stone in stones:
            bucket[stone] += 1
        
        first = max_stone
        second = max_stone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first - 1, second)

            while j > 0 and bucket[j] == 0:
                j -= 1
            
            if j == 0:
                return first
            
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)

        return first

    # TC -> O(N * Log(N))
    # SC -> O(N)
    # N -> len of stones list
    def __last_stone_weight_heap(self, stones: List[int]) -> int:
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