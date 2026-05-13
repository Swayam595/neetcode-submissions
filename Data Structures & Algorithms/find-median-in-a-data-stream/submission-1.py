class MedianFinder:

    def __init__(self):
        self.__small_heap = []          # Max Heap to keep all the values smaller than median
        self.__large_heap = []          # Min Heap to keep all the values larger than median

    def addNum(self, num: int) -> None:
        if len(self.__large_heap) > 0 and num > self.__large_heap[0]:
            heapq.heappush(self.__large_heap, num)
        else:
            heapq.heappush(self.__small_heap, -1 * num)

        if len(self.__small_heap) > len(self.__large_heap) + 1:
            val = -1 * heapq.heappop(self.__small_heap)
            heapq.heappush(self.__large_heap, val)
        
        if len(self.__large_heap) > len(self.__small_heap) + 1:
            val = heapq.heappop(self.__large_heap)
            heapq.heappush(self.__small_heap, -1 * val)

    def findMedian(self) -> float:
        if len(self.__small_heap) > len(self.__large_heap):
            return -1 * self.__small_heap[0]
        elif len(self.__small_heap) < len(self.__large_heap):
            return self.__large_heap[0]
            
        return (-1 * self.__small_heap[0] + self.__large_heap[0]) / 2
        