import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.__min_heap = []
        self.__k = k

        for num in nums:
            if len(self.__min_heap) < k:
                heapq.heappush(self.__min_heap, num)
            elif self.__min_heap[0] < num:
                self.__heapPopAndPush(num)

    def add(self, val: int) -> int:
        if len(self.__min_heap) == 0 or len(self.__min_heap) < self.__k:
            heapq.heappush(self.__min_heap, val)
        elif self.__min_heap[0] < val:
            self.__heapPopAndPush(val)
        return self.__min_heap[0]
    
    def __heapPopAndPush(self, val):
        heapq.heappop(self.__min_heap)
        heapq.heappush(self.__min_heap, val)   
        return     