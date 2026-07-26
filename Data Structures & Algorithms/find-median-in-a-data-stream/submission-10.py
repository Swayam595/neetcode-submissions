class MedianFinder:

    def __init__(self):
        self.__large = []
        self.__small = []

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

    def findMedian(self) -> float:
        if len(self.__small) > len(self.__large):
            return -self.__small[0]
        
        if len(self.__large) > len(self.__small):
            return self.__large[0]
        
        return (self.__large[0] - self.__small[0]) / 2