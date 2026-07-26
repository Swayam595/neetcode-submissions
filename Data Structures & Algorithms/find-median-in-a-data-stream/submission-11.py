class MedianFinder:

    def __init__(self):
        self.__large = []   # Min Heap
        self.__small = []   # Max Heap
    
    # TC -> O(log(N))
    # SC -> O(N)
    # N -> number of elements in the input
    def addNum(self, num: int) -> None:
        if len(self.__small) > 0 and -self.__small[0] > num:
            heapq.heappush(self.__small, -num)
        else:
            heapq.heappush(self.__large, num)

        if len(self.__small) > len(self.__large) + 1:
            val = -heapq.heappop(self.__small)
            heapq.heappush(self.__large, val)
        
        if len(self.__large) > len(self.__small) + 1:
            val = heapq.heappop(self.__large)
            heapq.heappush(self.__small, -val)
    
    # TC -> O(1)
    # SC -> O(1)
    def findMedian(self) -> float:
        if len(self.__small) > len(self.__large):
            return -self.__small[0]
        
        if len(self.__large) > len(self.__small):
            return self.__large[0]
        
        return (self.__large[0] - self.__small[0]) / 2