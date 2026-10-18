class MedianFinder:

    def __init__(self):
        self.__right_min_heap = []
        self.__left_max_heap = []
        
    # TC -> O(log * (N))
    # SC -> O(1)
    # N -> total number of nums in the 2 heaps
    def addNum(self, num: int) -> None:
        if len(self.__left_max_heap) > 0 and -self.__left_max_heap[0] > num:
            heapq.heappush(self.__left_max_heap, -num)
        else:
            heapq.heappush(self.__right_min_heap, num)
        
        if len(self.__left_max_heap) > len(self.__right_min_heap) + 1:
            val = -heapq.heappop(self.__left_max_heap)
            heapq.heappush(self.__right_min_heap, val)
        
        if len(self.__right_min_heap) > len(self.__left_max_heap) + 1:
            val = heapq.heappop(self.__right_min_heap)
            heapq.heappush(self.__left_max_heap, -val)
        
    # TC -> O(1)
    # SC -> O(1)
    def findMedian(self) -> float:
        if len(self.__left_max_heap) > len(self.__right_min_heap):
            return -self.__left_max_heap[0]
        
        if len(self.__left_max_heap) < len(self.__right_min_heap):
            return self.__right_min_heap[0]

        return (-self.__left_max_heap[0] + self.__right_min_heap[0]) / 2
        