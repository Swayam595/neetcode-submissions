import heapq
class MedianFinder:

    def __init__(self):
        self.__min_heap = []
        self.__max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.__min_heap) > 0 and num > self.__min_heap[0]:
            heapq.heappush(self.__min_heap, num)
        else:
            heapq.heappush(self.__max_heap, -num)

        if len(self.__max_heap) > len(self.__min_heap) + 1:
            val = -1 * heapq.heappop(self.__max_heap)
            heapq.heappush(self.__min_heap, val)
        
        if len(self.__min_heap) > len(self.__max_heap) + 1:
            val = heapq.heappop(self.__min_heap)
            heapq.heappush(self.__max_heap, -val)
            
    def findMedian(self) -> float:
        if len(self.__min_heap) > len(self.__max_heap):
            return self.__min_heap[0]
        
        if len(self.__max_heap) > len(self.__min_heap):
            return -self.__max_heap[0]

        return (-1 * self.__max_heap[0] + self.__min_heap[0]) / 2
        